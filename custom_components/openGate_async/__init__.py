from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
import aiohttp
import logging

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

    return True
 
