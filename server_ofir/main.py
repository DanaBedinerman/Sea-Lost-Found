import database_service_class
import meteorology
import physics
import time


def single_run(database_service, item_id, past_time):
    data = database_service.get_item_latest_history(item_id)
    string = str(data['latitude']) + ',' + str(data['longitude'])
    meteorology_data = meteorology.get_data('now', 'ocean_current_speed:kmh,ocean_current_direction:d', string)
    result = physics.getLocationAndRadius(data['latitude'], data['longitude'], meteorology_data['speed'],
                                          time.time() - past_time, meteorology_data['direction'], data['radius'])
    past_time = time.time()
    database_service.add_to_item_history(item_id, result['latitude'], result['longitude'], meteorology_data['direction'],
                                         meteorology_data['speed'], result['radius'])

    return past_time


if __name__ == '__main__':
    database_service = database_service_class.DatabaseServiceClass()
    lost_item_id = database_service.create_new_item()

    for n in range(100):
        past_time = time.time()
        past_time = single_run(database_service, lost_item_id, past_time)
        time.sleep(30)
