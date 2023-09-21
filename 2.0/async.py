import asyncio


async def main():
    task = asyncio.create_task(doSomething())
    print('A')
    await asyncio.sleep(1)
    print("B")
    await task


async def doSomething():
    print("1")
    await asyncio.sleep(2)
    print("2")


asyncio.run(main())
