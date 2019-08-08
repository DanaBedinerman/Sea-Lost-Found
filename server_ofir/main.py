import database_service_class
import meteorology
import physics
import time
from aiohttp import web
import socketio
import json

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
meteorology_data = {}
result = {}

def single_run(database_service, item_id, past_time):
    data = database_service.get_item_latest_history(item_id)
    string = str(data['latitude']) + ',' + str(data['longitude'])
    meteorology_data = meteorology.get_data('now', 'ocean_current_speed:kmh,ocean_current_direction:d', string)
    result = physics.getLocationAndRadius(data['latitude'], data['longitude'], meteorology_data['speed'],
                                          time.time() - past_time, meteorology_data['direction'], data['radius'])
    past_time = time.time()
    database_service.add_to_item_history(item_id, result['latitude'], result['longitude'], meteorology_data['direction'],
                                         meteorology_data['speed'], result['radius'])

    print('item id: ',item_id)
    print({ 'latitude': result['latitude'], 'longitude': result['longitude'] })
    print('radius: ',result['radius'])
    print('direction: ',meteorology_data['direction'])
    print('message sent')

    return past_time

@sio.on('location')
async def get_locations(sid, message):
    print ('got location request')
    database_service = database_service_class.DatabaseServiceClass()
    lost_item_id = database_service.create_new_item()

    for n in range(100):
        past_time = time.time()
        past_time = single_run(database_service, lost_item_id, past_time)
        await sio.emit(lost_item_id, { 'latitude': result['latitude'], 'longitude': result['longitude'] }, result['radius'], meteorology_data['direction'])
        time.sleep(5)

if __name__ == '__main__':
    print('1')
    web.run_app(app)
    # database_service = database_service_class.DatabaseServiceClass()
    # lost_item_id = database_service.create_new_item()

    # for n in range(100):
    #     past_time = time.time()
    #     past_time = single_run(database_service, lost_item_id, past_time)
    #     time.sleep(5)
