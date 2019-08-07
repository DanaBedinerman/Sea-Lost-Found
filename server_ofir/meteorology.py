# Imports.
import requests
import json

# Constants.
USERNAME = 'mefatzeahegozim_balonim'
PASSWORD = 'GV163WxgPajDe'


def get_data(time, params, location):
    """input:
        timestamp, API parameters, location in longtitude, latitude.
        output:
        api response
    """
    # Url format
    url = 'http://{}:{}@api.meteomatics.com'.format(USERNAME, PASSWORD)

    # Get data from api, load it to json
    r = requests.get('{}/{}/{}/{}/{}'.format(url, time, params, location, 'json'))
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
    export_data = {
        "speed": ocean_current_speed_ms,
        "direction": ocean_current_direction
    }
    return export_data
    # print(export_data["results"])
