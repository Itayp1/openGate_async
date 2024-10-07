"""Button platform for openGate."""

import logging
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import EntityCategory
import aiohttp

from .const import DOMAIN_DATA, KETTLE_ICON, BACKENDAPI

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setup button platform."""

    sensors = []
    sensors.append(BoileWater(hass, "Boil Water"))
    async_add_entities(sensors, True)


class BoileWater(ButtonEntity):
    """boil button."""

    def __init__(self, hass, name):
        self.hass = hass
        self.handler = self.hass.data[DOMAIN_DATA]["handler"]
        self._name = name
        self._state = None
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_unique_id = "openGate_boil_water"

    async def async_press(self) -> None:
        """Press the button."""
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

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        return KETTLE_ICON

 