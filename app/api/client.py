
from typing import Any, Optional
from app.utils import logger

import aiohttp

class APIClient:
    BASE_URL = "http://127.0.0.1:9090"
    
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None
        self.timeout = aiohttp.ClientTimeout(total=10.0)

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=self.timeout)
        return self._session

    async def request(self, endpoint: str, arg: str) -> Any:
        url = f"{self.BASE_URL}/services/{endpoint}"
        params = {"text": arg}

        session = await self._get_session()

        try:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    logger.success(f"API request successful: {url}")
                    data = await response.json()
                    return data.get("data")
                else:
                    logger.error(f"API error: {response.status}")
                    return "ошибка"
        except Exception as e:
            logger.error(f"network error: {e}")
            return f"ошибка сети: {e}"

    async def close(self):
        if self._session:
            await self._session.close()

client = APIClient()