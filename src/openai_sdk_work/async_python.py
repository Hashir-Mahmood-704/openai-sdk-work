import time
import asyncio


async def makeCoffee() -> str:
    print("Started making coffee")
    # time.sleep(2)
    await asyncio.sleep(4)
    print("Ended making coffee")
    return "coffee ready"


async def toastBread() -> str:
    print("Started toasting bread")
    # time.sleep(1)
    await asyncio.sleep(2)
    print("Ended toasting bread")
    return "toast ready"


async def main():
    print("Running async python file")
    startTime = time.time()
    # coffeeResult, toastResult = await asyncio.gather(makeCoffee(), toastBread())
    
    callCoffeeMaker = asyncio.create_task(makeCoffee())
    callToastMaker = asyncio.create_task(toastBread())

    coffeeResult = await callCoffeeMaker
    toastResult = await callToastMaker

    endTime = time.time()

    print(coffeeResult)
    print(toastResult)
    print(f"Time used: {endTime - startTime:.3f}")


def runMain():
    asyncio.run(main())
