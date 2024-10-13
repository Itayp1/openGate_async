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

            url = f"{BACKENDAPI}/gates/callNow?uqid={self.uqid}&gateId={self.gateId}&type=manualCall&userLocation=undefined"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                         return  True
                    
 
 

        except Exception as e:
            raise Exception(
                f"Failed to communicate with API due to time out {str(e)}"
            )
 


 