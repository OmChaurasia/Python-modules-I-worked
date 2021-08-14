from pyppeteer import launch
from bs4 import BeautifulSoup
import asyncio
import time

async def main(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.amazon.in/hfc/bill/lpg?ref=hfc_buyx_red")
    await page.mouse.click(400,278)
    time.sleep(1)
    await page.mouse.click(400,285)
    time.sleep(3)
    await page.evaluate('''
        document.getElementById('LpgId/RMN').value="7309370691"
    ''')
    await page.keyboard.press("Enter")
    # await page.type('[id=searchInput]',keyword)
    
    await page.screenshot({"path": "main_page.png"})
    # await page.screenshot({"path": "result.png"})
    # urls = await page.evaluate('''
    
    # ''')

    await browser.close()

asyncio.get_event_loop().run_until_complete(main('cat'))