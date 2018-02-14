""" Turns on the TV and selects a source """


# get params
source_command = data.get('source_command')

tv_switch_entity = 'switch.tv_power'
states = hass.states.get(tv_switch_entity)

while states.state == 'off':
	# turn on the tv
	input_data = {'entity_id': tv_switch_entity}
	hass.services.call('switch', 'turn_on', input_data)
	states = hass.states.get(tv_switch_entity)

# run the given rest command
hass.services.call('rest_command', source_command)