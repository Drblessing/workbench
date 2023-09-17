import asyncio
from web3 import AsyncWeb3
import logging

# Init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Format logger
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
# Create file handler
file_handler = logging.FileHandler("reth_async_requests.log")
file_handler.setFormatter(formatter)
# Add file handler to logger
logger.addHandler(file_handler)

# Add logger init message
logger.info("Init logger")

w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider("http://69.67.151.138:8645"))

# Check w3 is connected


# async def get_balance(address):
#     return await w3.eth.getBalance(address)


# async def check_all_balances(address):
#     # Create 1000 coroutines to get the balance
#     tasks = [get_balance(address) for _ in range(1000)]

#     # Execute all coroutines concurrently
#     balances = await asyncio.gather(*tasks)

#     # Check if all balances are the same
#     return all(balance == balances[0] for balance in balances)


# # Example usage:
# address = "YOUR_WALLET_ADDRESS"
# result = asyncio.run(check_all_balances(address))
# if result:
#     print("All balances are the same!")
# else:
#     print("Balances are different!")
