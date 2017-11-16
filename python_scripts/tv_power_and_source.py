""" Turns on the TV and selects a source """


# get params
source_command = data.get('source_command')

# turn on the tv
input_data = {'entity_id': 'input_boolean.tv'}
hass.services.call('input_boolean', 'turn_on', input_data)

# run the given rest command
hass.services.call('rest_command', source_command)