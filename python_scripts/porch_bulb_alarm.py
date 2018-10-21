"""Flash porch bulb red"""

logger.debug("")
logger.debug("")
logger.debug("START PORCH ALARM")

red = [255, 0, 0]
white = [255, 255, 255]

bulb_id = 'light.porch_bulb'
switch_id = 'switch.entry_lights_porch'


def change_color(hass, color, brightness, logger=None):
	if logger:
		logger.debug("Turning bulb {} @ {}".format(color, brightness))
	global bulb_id
	input_data = {"entity_id": bulb_id, "rgb_color": color, "brightness": brightness}
	hass.services.call('light', 'turn_on', input_data)
	time.sleep(1)
	

switch_state = hass.states.get(switch_id)
#logger.debug("Switch state {}".format(switch_state))

orig_switch = switch_state.state
#logger.debug("Orig switch {}".format(orig_switch))

# turn on the porch light
if orig_switch == 'off':
	logger.debug('Turn on porch light')
	input_data = {"entity_id" : switch_id}
	hass.services.call('switch', 'turn_on', input_data)

states = hass.states.get(bulb_id)
#logger.debug(states)
original_color = states.attributes.get('rgb_color')
brightness = states.attributes.get('brightness')

# change color if it's already on
if original_color:
	original_color = [original_color[0], original_color[1], original_color[2]]
	logger.debug("Bulb originally {} @ {}".format(original_color, brightness))

	change_color(hass, red, 255, logger)
	change_color(hass, white, 255, logger)
	change_color(hass, red, 255, logger)
	change_color(hass, white, 255, logger)
	change_color(hass, red, 255, logger)
	change_color(hass, white, 255, logger)
	change_color(hass, red, 255, logger)

	change_color(hass, original_color, brightness, logger)

# just blink if it was off or we can't get the color
else:
	logger.info('blink porch light')
	input_data = {"entity_id" : switch_id}
	hass.services.call('switch', 'turn_off', input_data)
	time.sleep(1)
	hass.services.call('switch', 'turn_on', input_data)
	time.sleep(1)
	hass.services.call('switch', 'turn_off', input_data)
	time.sleep(1)
	hass.services.call('switch', 'turn_on', input_data)
	time.sleep(1)
	hass.services.call('switch', 'turn_off', input_data)
	time.sleep(1)
	hass.services.call('switch', 'turn_on', input_data)
	time.sleep(1)	
	
# turn off the porch light if it was off
if orig_switch == 'off':
	logger.debug('Turn off porch light')
	input_data = {"entity_id" : switch_id}
	hass.services.call('switch', 'turn_off', input_data)