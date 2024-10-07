import aiohttp
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import Entity
BACKENDAPI = "http://10.100.102.10:3000"
class MyApiButton(ButtonEntity):
    """Representation of a Button that triggers an API call."""

    def __init__(self, name: str):
        self._name = name
        self._unique_id = "api_button_unique_id"

    @property
    def name(self) -> str:
        """Return the name of the button."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the button."""
        return self._unique_id

    async def async_press(self):
        """Handle the button press."""
        await self.trigger_api_call()

    async def trigger_api_call(self):
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
            return False