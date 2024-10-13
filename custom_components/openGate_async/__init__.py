from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
# from homeassistant.helpers.entity_platform import async_add_entities
 

import aiohttp
import logging
from .api_button import MyApiButton

DOMAIN = "openGate_async"
BACKENDAPI = "http://10.100.102.10:3000"
_LOGGER = logging.getLogger(__name__)

from .API import openGateApi




 

async def async_setup_entry(hass: HomeAssistant, config_entry ):
    # uqid = entry.data["uqid"]
    # hass.states.async_set(f"{DOMAIN}.uqid", uqid)
    gateId = config_entry.data.get("gateId")
    uqid = config_entry.data.get("uqid")
    # gateId = entry.data["gateId"]
    # hass.states.async_set(f"{DOMAIN}.gateId", gateId)
    client = openGateApi(uqid, gateId)

    async def handle_my_service(call):
        uqid = call.data.get("uqid")
        # Add logic for your service here
        # hass.states.set("openGate_async.last_service_call", my_param)
        """Make an API call when the button is pressed."""
        try:
            url = f"{BACKENDAPI}/addresses/{uqid}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return True
                    return False
        except Exception as e:
            _LOGGER.error("Error during API call: %s", e)
        return True

    hass.services.async_register(DOMAIN, "my_custom_service", client.open_gate)

    # button = MyApiButton(config_entry)
    # hass.data[DOMAIN] = {}
    # hass.data[DOMAIN]['open_gate_button'] = MyApiButton(config_entry)
    # # async_add_entities([button])
    # hass.data.setdefault(DOMAIN, []).append(button)
    # async_add_entities([MyApiButton(hass, "My Custom Button")])
        # Add entity to the Home Assistant entity registry
    # await hass.helpers.entity_registry.async_get_or_create(
    #     "button",  # Domain for the entity
    #     DOMAIN,    # Unique identifier for your integration
    #     "open_gate_button",  # Unique ID for the button
    #     suggested_object_id="open_gate_button",  # Optional: custom ID
    #     name="Open Gate Button"  # Optional: display name
    # )
    # async_add_entities([button])

    return True
 
