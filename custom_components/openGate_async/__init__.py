from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity

DOMAIN = "openGate_async"

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    phone_number = entry.data["phone_number"]
    hass.states.async_set(f"{DOMAIN}.phone_number", phone_number)
    return True
