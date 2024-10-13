from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .config_flow import MyClimateConfigFlow  # Import your config flow class
from .climate import MyClimate  # Import your climate entity class

DOMAIN = "my_climate"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the climate component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up climate entity from a config entry."""
    # Create a platform for the climate entity directly
    hass.data.setdefault(DOMAIN, {})  # Create a dictionary to store data
    my_climate_entity = MyClimate()  # Create an instance of your climate entity
    hass.data[DOMAIN]['entities'] = hass.data[DOMAIN].get('entities', [])
    hass.data[DOMAIN]['entities'].append(my_climate_entity)  # Store the entity for later use

    return True

# Register the config flow handler
config_entries.HANDLERS.register(DOMAIN)(MyClimateConfigFlow)
