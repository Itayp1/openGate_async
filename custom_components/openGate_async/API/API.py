"""openGate API client"""
import asyncio
import logging
from json import JSONDecodeError
import aiohttp
from ..const import   BACKENDAPI

_LOGGER = logging.getLogger(__name__)


class openGateApiError(Exception):
    pass


class openGateApi:

    def __init__(self, uqid, gateId):
        self.uqid = uqid
        self.gateId = gateId
 

    async def open_gate(self , anyVar) -> dict:
        try:

            url = f"{BACKENDAPI}/addresses/{self.uqid}/{self.gateId}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        result = await response.json()
                        return  result[0]['gates'][0]['_id']
                    
 
 

        except Exception as e:
            raise openGateApiError(
                f"Failed to communicate with API due to time out {str(e)}"
            )
 

        return False

 