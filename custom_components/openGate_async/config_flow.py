import voluptuous as vol
from homeassistant import config_entries
import aiohttp
import logging

DOMAIN = "openGate_async"
BACKENDAPI = "http://10.100.102.10:3000"

_LOGGER = logging.getLogger(__name__)

class OpenGateAsyncConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        """Step to ask for the phone number."""
        if user_input is not None:
            self.phone_number = user_input["phone_number"]
            try:
                if await self.call_rest_api(self.phone_number):
                    return await self.async_step_otp()
            except Exception as e:
                _LOGGER.error("Error during API call: %s", e)
                return self.async_show_form(
                    step_id="user",
                    errors={"base": "error_api"},
                    data_schema=vol.Schema({vol.Required("phone_number"): str}),
                )            
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("phone_number"): str}),
        )

    async def async_step_otp(self, user_input=None):
        """Step to ask for OTP code."""
        if user_input is not None:
            otp_code = user_input["otp_code"]
            self.uqid = await self.verify_otp(self.phone_number, otp_code)
            if self.uqid:
                return self.async_create_entry(title="Open Gate", data={"uqid": self.uqid})
            return self.async_show_form(
                step_id="otp",
                errors={"base": "invalid_code"},
                data_schema=vol.Schema({vol.Required("otp_code"): str}),
            )
        return self.async_show_form(
            step_id="otp",
            data_schema=vol.Schema({vol.Required("otp_code"): str}),
        )

    async def call_rest_api(self, phone_number):
        """Function to call API to send OTP."""
        try:
            url = f"{BACKENDAPI}/sms/generateSmsCode"
            data = {"ext": "972", "phone": phone_number}
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        return True
                    return False
        except Exception as e:
            _LOGGER.error("Error during API call: %s", e)
            return False

    async def verify_otp(self, phone_number, otp_code):
        """Function to verify OTP code via API."""
        try:
            url = f"{BACKENDAPI}/sms/verifySmsCode"
            data = {
                "ext": "972",
                "phone": phone_number,
                "smsCode": otp_code,
                "platform": "android",
                "deviceVersion": "14",
                "deviceType": "samsung"
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result.get("uqid")
                    return False
        except Exception as e:
            _LOGGER.error("Error during OTP verification: %s", e)
            return False
