from homeassistant import config_entries

@config_entries.HANDLERS.register("tornado")
class MyClimateConfigFlow(config_entries.ConfigFlow):
    """Handle a config flow for My Climate."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        return self.async_create_entry(title="My Climate", data={})
