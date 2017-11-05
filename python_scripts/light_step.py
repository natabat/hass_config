""" Turns on and brightens a light over time """

# get params
entity_id = data.get('entity_id')
step = int(data.get('step'))

# Get current brightness value
states = hass.states.get(entity_id)
brightness = states.attributes.get('brightness') or 0

dim = brightness + step
if dim < 0: dim = 0
if dim > 255: dim = 255

if dim == 0:
	input_data = {"entity_id": entity_id}
	hass.services.call('light', 'turn_off', input_data)
else:
	input_data = {"entity_id" : entity_id, "brightness": dim}
	hass.services.call('light', 'turn_on', input_data)


