import voluptuous as vol
from homeassistant import config_entries
import aiohttp
import requests


DOMAIN = "openGate_async"

class OpenGateAsyncConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        """Step to ask for the phone number."""
        if user_input is not None:
            self.phone_number = user_input["phone_number"]

            # Call the API to send OTP to phone number
            if await self.call_rest_api(self.phone_number):
                # Proceed to OTP verification step
                return await self.async_step_otp()

        # Show form to request phone number input
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("phone_number"): str,
            })
        )

    async def async_step_otp(self, user_input=None):
        """Step to ask for OTP code."""
        if user_input is not None:
            otp_code = user_input["otp_code"]

            # Verify the OTP code via API
            if await self.verify_otp(self.phone_number ,otp_code):
                # Create an entry with valid data
                return self.async_create_entry(title="Verified", data=user_input)
            else:
                return self.async_show_form(
                    step_id="otp",
                    errors={"base": "invalid_code"},
                    data_schema=vol.Schema({
                        vol.Required("otp_code"): str,
                    })
                )

        # Show form to request OTP code input
        return self.async_show_form(
            step_id="otp",
            data_schema=vol.Schema({
                vol.Required("otp_code"): str,
            })
        )

    async def call_rest_api(self, phone_number):
        """Function to call API to send OTP."""
        try:
            url = "https://api.opengate.io/sms/generateSmsCode"
            data = {
                "ext": "972",
                "phone":phone_number
            }
            response = requests.post(url, json=data)
            # Check if the request was successful
            if response.status_code == 200:
                print("Success:", response.json())
                return True
            else:
                print(f"Failed with status code {response.status_code}: {response.text}")
                return False
        except Exception as e:
            # Handle any exceptions or errors from the API
            return False

    async def verify_otp(self, phone_number ,otp_code):
        """Function to verify OTP code via API."""
        try:
            url = "https://api.opengate.io/sms/verifySmsCode"
            data = {"ext":"972","phone":phone_number,"smsCode":otp_code,"platform":"android","deviceVersion":"14","deviceType":"samsung"}
            response = requests.post(url, json=data)
            # Check if the request was successful
            if response.status_code == 200:
                print("Success:", response.json())
                result = response.json()
                uqid = result.get("uqid")
                return uqid
            else:
                print(f"Failed with status code {response.status_code}: {response.text}")
                return False
        except Exception as e:
            # Handle any exceptions or errors from the API
            return False
