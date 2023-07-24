import asyncio

import aiohttp


async def Captcha_Solver(captcha_key):
    async with aiohttp.ClientSession() as session:
        session.headers.update({"Content-Type": "application/json"})
        json_data_send = {
            "key": f"{captcha_key}",
            "method": "userrecaptcha",
            "googlekey": "6LeikZgeAAAAAFWZu0Uw3u6to9M_MEwEBC5jMirK",
            "pageurl": "https://api.myataofficial.com/v6/auth/token",
            "json": 1
        }
        async with session.post("https://api.captcha.guru/in.php", json=json_data_send) as response:
            request_id = (await response.json())["request"]

        json_data_get = {
            "key": f"{captcha_key}",
            "action": "get",
            "id": f"{request_id}",
            "json": 1
        }

        while captcha_key == "CAPCHA_NOT_READY":
            async with session.post("https://api.captcha.guru/res.php", json=json_data_get) as response:
                captcha_key = (await response.json())["request"]
                await asyncio.sleep(5)

        return captcha_key
