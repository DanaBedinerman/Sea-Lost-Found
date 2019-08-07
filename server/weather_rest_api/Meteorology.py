# Imports.
import requests
import json

# Constants.
USERNAME = 'mefatzeahegozim_balonim'
PASSWORD = 'GV163WxgPajDe'


def main():

    # Url format
    url = 'http://{}:{}@api.meteomatics.com'.format(USERNAME, PASSWORD)

    # Parameters
    time = 'now'
    params = 'ocean_current_speed:kmh,ocean_current_direction:d'
    location = '32.843265,35.013531'  # Latitude, longitude.
    form = 'json'

    # Get data from api, load it to json
    r = requests.get('{}/{}/{}/{}/{}'.format(url, time, params, location, form))
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
    print(export_data["results"])


def send_results():
    pass


if __name__ == '__main__':
    main()
