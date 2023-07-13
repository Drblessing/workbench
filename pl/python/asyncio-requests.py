# Send 10 requests asynchronously and print the result
import asyncio
import aiohttp

c = 0
URL = "https://camo.githubusercontent.com/ceb7faeb7a45a2abc72dbbf013b192c762260c1dd33c774d10f91a9a7c8ee139/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d73696d656f6e6f6e7365637572697479"


async def fetch(session, url=URL):
    async with session.get(url) as response:
        print("Sending request...")
        response.raise_for_status()
        text = await response.text()
        response_number = int(text.split("</text>")[-2].split(">")[-1].replace(",", ""))
        return response_number


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.ensure_future(fetch(session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        count = len(responses)
        print(f"Received {count} responses")
        print(responses)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
