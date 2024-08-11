import re
import sys
import time
import traceback
from sys import stdout

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def main():
    print("init chrome options")
    url = f"https://kaspi.kz/shop/search/?text=121182195&q=%3AavailableInZones%3AMagnum_ZONE1&sort=relevance&filteredByCategory=false&sc="
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.binary_location = "/usr/bin/google-chrome"
    print("init chrome driver")
    driver = webdriver.Chrome(
        options=chrome_options
    )
    print("open url")
    driver.get(url)
    print(f"Opened URL: {url}")
    print(f"Page title: {driver.title}")
    print(
        f"driver title is 'Поиск 121182195 | Kaspi Магазин'?\n "
        f"{driver.title == 'Поиск 121182195 | Kaspi Магазин'}"
    )


if __name__ == "__main__":
    main()
