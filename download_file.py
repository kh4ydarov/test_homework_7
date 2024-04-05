import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\Users\\sarvar\\PycharmProjects\\test_homework_7\\tmp",  # Путь для скачивание
    "download-prompt_for_download": False  # Игнорирование подтверждении скачивании
}

options.add_experimental_option("prefs", prefs)  # Добавление экспериментального опции

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Создали драйвер
browser.config.driver = driver  # Присвоили драйвер который мы создали

browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
browser.element("[data-testid='download-raw-button']").click()

time.sleep(10)
