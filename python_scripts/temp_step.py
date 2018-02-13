""" Adjusts a target temp """

# get params
entity_id = data.get('entity_id')
target_temp = data.get('target_temp')
step = data.get('step')

temp_attribute = 'target_temp_' + target_temp

# Get current brightness value
states = hass.states.get(entity_id)
target = states.attributes.get(temp_attribute)
temperature = states.attributes.get('current_temperature')
temp_high = states.attributes.get('target_temp_high')
temp_low = states.attributes.get('target_temp_low')

new_temp = target + step


if temp_attribute == 'target_temp_high':
	temp_high = new_temp
if temp_attribute == 'target_temp_low':
	temp_low = new_temp

logger.info("{} from {} to {}".format(temp_attribute, target, new_temp))

input_data = {"entity_id" : entity_id, 'temperature' : temperature, 'target_temp_high': temp_high, 'target_temp_low': temp_low }
hass.services.call('climate', 'set_temperature', input_data)


