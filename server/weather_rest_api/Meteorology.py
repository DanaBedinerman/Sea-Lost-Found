# Imports.
import requests
import json
import pika, logging, sys, argparse, time
from time import sleep
from argparse import RawTextHelpFormatter

# Constants.
USERNAME = 'mefatzeahegozim_balonim'
PASSWORD = 'GV163WxgPajDe'

# Global
q = ''
q_name = ''


def on_message(channel, method_frame, header_frame, body):

    # Url format
    url = 'http://{}:{}@api.meteomatics.com'.format(USERNAME, PASSWORD)

    # Parse Body.
    param_json = json.loads(body)

    # Parameters
    time_ = param_json['time'] if param_json['time'] else 'now'
    params = 'ocean_current_speed:kmh,ocean_current_direction:d'
    location = param_json['location']  # Latitude, longitude.
    form = 'json'

    # Get data from api, load it to json
    r = requests.get('{}/{}/{}/{}/{}'.format(url, time_, params, location, form))
    data = json.loads(r.text)

    # Turning results to variables
    if data['data'][0]['parameter'] == 'ocean_current_speed:kmh':
        ocean_current_speed_kmh = data['data'][0]['coordinates'][0]['dates'][0]['value']
        ocean_current_speed_ms = ocean_current_speed_kmh / 3.6
    else:
        ocean_current_speed_ms = -999

    if data['data'][1]['parameter'] == 'ocean_current_direction:d':
        ocean_current_direction = data['data'][1]['coordinates'][0]['dates'][0]['value']
    else:
        ocean_current_direction = -999

    # Final json.
    export_data = {"results": {"ocean_current_speed_ms": ocean_current_speed_ms,
                               "ocean_current_direction": ocean_current_direction}}
    channel.basic_publish('', q_name, json.dumps(export_data))
    # print(export_data["results"])


def send_results():
    pass


if __name__ == '__main__':
    examples = sys.argv[0] + " -p 5672 -s rabbitmq "
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description='Run consumer.py',
                                     epilog=examples)
    parser.add_argument('-p', '--port', action='store', dest='port', help='The port to listen on.')
    parser.add_argument('-s', '--server', action='store', dest='server', help='The RabbitMQ server.')

    args = parser.parse_args()
    if args.port == None:
        print("Missing required argument: -p/--port")
        sys.exit(1)
    if args.server == None:
        print("Missing required argument: -s/--server")
        sys.exit(1)

    # sleep a few seconds to allow RabbitMQ server to come up
    sleep(5)
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(args.server,
                                           int(args.port),
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    q = channel.queue_declare('pc')
    q_name = q.method.queue
    channel.confirm_delivery()
    channel.basic_consume(on_message, 'pc')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
