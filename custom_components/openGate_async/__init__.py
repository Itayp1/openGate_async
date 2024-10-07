from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import async_add_entities
 

import aiohttp
import logging
from .api_button import MyApiButton

DOMAIN = "openGate_async"
BACKENDAPI = "http://10.100.102.10:3000"
_LOGGER = logging.getLogger(__name__)





async def async_setup(hass: HomeAssistant, config: dict):
  
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    # uqid = entry.data["uqid"]
    # hass.states.async_set(f"{DOMAIN}.uqid", uqid)

    # gateId = entry.data["gateId"]
    # hass.states.async_set(f"{DOMAIN}.gateId", gateId)

    async def handle_my_service(call):
        # my_param = call.data.get("my_param")
        # Add logic for your service here
        # hass.states.set("openGate_async.last_service_call", my_param)
        """Make an API call when the button is pressed."""
        try:
            url = f"{BACKENDAPI}/addresses"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return True
                    return False
        except Exception as e:
            _LOGGER.error("Error during API call: %s", e)
        return True

    hass.services.async_register("openGate_async", "my_custom_service", handle_my_service)

    button = MyApiButton("Trigger API Call")
    hass.data[DOMAIN] = button
    # async_add_entities([button])
    hass.data.setdefault(DOMAIN, []).append(button)
    async_add_entities([MyApiButton(hass, "My Custom Button")])
    return True
 
