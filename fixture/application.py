from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
import logging
from fixture.blocks import Blockhelper

logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(2)
        self.exceptions = exceptions
        self.waits = WebDriverWait
        self.log = logging
        self.log.info('Запуск тестов')
        self.blocks = Blockhelper(self)


    def open_test_page(self):
        wd = self.wd
        if wd.current_url != 'http://blog.csssr.ru/qa-engineer/':
            wd.get('http://blog.csssr.ru/qa-engineer/')
            self.log.info('Открываем тестируемую страницу')

    def destroy(self):
        self.wd.quit()
        self.log.info('Тесты завершены')

