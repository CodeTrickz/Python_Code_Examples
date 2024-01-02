import asyncio


async def async_generator():
    for i in range(5):
        print(f"Yielding value {i}")
        yield i
        await asyncio.sleep(1)


async def main():
    async for value in async_generator():
        print(f"Received value: {value}")

# Asynchrone loop starten
asyncio.run(main())
