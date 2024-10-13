from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_OFF, HVAC_MODE_HEAT, SUPPORT_TARGET_TEMPERATURE
)
from homeassistant.const import TEMP_CELSIUS, ATTR_TEMPERATURE

class MyClimate(ClimateEntity):
    def __init__(self):
        """Initialize the climate device."""
        self._name = "My Climate Device"
        self._hvac_mode = HVAC_MODE_OFF
        self._target_temperature = 22
        self._current_temperature = 21
        self._supported_features = SUPPORT_TARGET_TEMPERATURE

    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    @property
    def hvac_modes(self):
        """Return the list of supported HVAC modes."""
        return [HVAC_MODE_OFF, HVAC_MODE_HEAT]

    @property
    def hvac_mode(self):
        """Return the current HVAC mode."""
        return self._hvac_mode

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return self._supported_features

    def set_hvac_mode(self, hvac_mode):
        """Set new target HVAC mode."""
        self._hvac_mode = hvac_mode
        self.schedule_update_ha_state()

    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        if ATTR_TEMPERATURE in kwargs:
            self._target_temperature = kwargs[ATTR_TEMPERATURE]
        self.schedule_update_ha_state()

    def update(self):
        """Fetch new state data for this climate device."""
        # Here you would add the logic to get the actual temperature from the hardware
        pass
