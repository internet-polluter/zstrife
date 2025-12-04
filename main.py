import asyncio
import zendriver as zd
import time


async def main():
    print("Hello WORLD!@!")
    browser = await zd.start()
    page = await browser.get('https://discord.com')
    time.sleep(10)
    await browser.stop()


if __name__ == "__main__":
    asyncio.run(main())
