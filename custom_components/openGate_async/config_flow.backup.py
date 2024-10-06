import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

class OpenGateConfigFlow(config_entries.ConfigFlow, domain="openGate_async"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Phone Number", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("phone_number"): str
            })
        )
