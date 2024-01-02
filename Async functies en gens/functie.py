import asyncio


async def async_function():
    print("Start async function")
    await asyncio.sleep(2)
    print("Async function completed after 2 seconds")


async def main():
    print("Main function started")
    await async_function()
    print("Main function completed")

# Asynchrone loop starten
asyncio.run(main())
