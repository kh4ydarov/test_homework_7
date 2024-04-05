import os
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
tmp_path = os.path.join(BASE_DIR, 'tmp\\')

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": tmp_path,  # Путь для скачивание
    "download-prompt_for_download": True  # Игнорирование подтверждении скачивании
}

options.add_experimental_option("prefs", prefs)  # Добавление экспериментального опции
options.add_argument('--download.default_directory=' + tmp_path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Создали драйвер
browser.config.driver = driver  # Присвоили драйвер который мы создали

browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
browser.element("[data-testid='download-raw-button']").click()

time.sleep(10)
