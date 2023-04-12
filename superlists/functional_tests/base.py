from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os


import time

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    '''функциональный тест'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        '''ожидать строку в таблице списка'''
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element('id','id_list_table')
                rows = table.find_elements('tag name','tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as errors:
                if time.time() - start_time > MAX_WAIT:
                    raise errors
                time.sleep(0.5)

    def wait_for(self, fn):
        '''ожидать строку в таблице списка'''
        start_time = time.time()
        while True:
            try:
                return(fn)
            except (AssertionError, WebDriverException) as errors:
                if time.time() - start_time > MAX_WAIT:
                    raise errors
                time.sleep(0.5)