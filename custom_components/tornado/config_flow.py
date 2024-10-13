import voluptuous as vol
from homeassistant import config_entries
import aiohttp
import logging

DOMAIN = "my_climate"
from .const import   BACKENDAPI

_LOGGER = logging.getLogger(__name__)

class MyClimateConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        """Step to ask for the phone number."""
        if user_input is not None:
            self.phone_number = user_input["phone_number"]
            return self.async_create_entry(title="my_climate", data={ "phone_number":self.phone_number})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("phone_number"): str}),
        )
