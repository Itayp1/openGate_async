async def async_setup(hass: HomeAssistant, config: dict):
    async def handle_button_press(call):
        await hass.async_add_executor_job(invoke_api)

    hass.services.async_register(DOMAIN, "press_button", handle_button_press)
    return True

def invoke_api():
    # Logic to call the API
    pass
