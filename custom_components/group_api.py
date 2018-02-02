"""
Rest API for Home Assistant.

For more details about the RESTful API, please refer to the documentation at
https://home-assistant.io/developers/api/
"""
import asyncio
import json
import logging

import async_timeout

import homeassistant.core as ha
from homeassistant.bootstrap import DATA_LOGGING
from homeassistant.const import (
    HTTP_NOT_FOUND, URL_API_ERROR_LOG,  __version__)
from homeassistant.components.http import HomeAssistantView

DOMAIN = 'group_api'
DEPENDENCIES = ['http']

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Register the API with the HTTP interface."""
    hass.http.register_view(APIGroupView)

    log_path = hass.data.get(DATA_LOGGING, None)
    if log_path:
        hass.http.register_static_path(URL_API_ERROR_LOG, log_path, False)

    return True
    
class GroupApiView(HomeAssistantView):
    """View to handle new api call"""
        
    url = "/api/members/{group_id}"
    name = "api:members"
    
    @asyncio.coroutine
    def get(self, request, group_id):
        """Handle GET request"""
        hass = request.app['hass']
        json_response = []
        
        group_state = hass.states.get(group_id)
        
        if group_state:
                for entity_id in group_state.attributes['entity_id']:
                    entity_state = hass.states.get(entity_id)
                    if entity_state:
                        json_response.append(entity_state)
            return self.json(json_response)
        
        return self.json_message('Group not found', HTTP_NOT_FOUND)