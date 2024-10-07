"""Constants for openGate."""

from datetime import timedelta
BACKENDAPI = "http://10.100.102.10:3000"

# Base component constants
DOMAIN = "openGate_async"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.1"
PLATFORMS = ["sensor", "button"]

# Volume units
VOLUME_LITERS = "L"
TIME_DAYS = "Days"

# Icons
WATER_ICON = "mdi:cup-water"
KETTLE_ICON = "mdi:kettle-steam-outline"
CALENDAR_ICON = "mdi:calendar"
SYNC_ICON = "mdi:sync-circle"

# Overall scan interval
TOKEN_SCAN_INTERVAL = timedelta(hours=3)
WATER_QUALITY_INTERVAL = timedelta(hours=8)
WATER_CONSUMPTION_INTERVAL = timedelta(hours=1)
