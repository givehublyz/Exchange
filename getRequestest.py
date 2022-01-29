from GetAllExchangePair import getAllExchangePair
from UpdateDataThread import GetRequestThread
import time
import asyncio
import async_timeout
import aiohttp

async def process(client, url):
    with async_timeout.timeout(1000):
        async with client.get(url) as response:
            return response

async def func(url):
    async with aiohttp.ClientSession() as client:
        res = await process(client, url)
        return res

BASE_URL = "https://api.binance.com"

exchangePair = getAllExchangePair()
# urls = []
# for item in exchangePair:
#     url = BASE_URL + "/api/v3/klines?symbol=" + item['symbol'] + "&interval=1d&limit=2"
#     urls.append(url)
#
# s = time.time()
# loop = asyncio.get_event_loop()
# tasks = [func(url) for url in urls]
# resList = loop.run_until_complete(asyncio.gather(*tasks))
#
# e = time.time()
# print("cost time:", e - s)
# print(resList)