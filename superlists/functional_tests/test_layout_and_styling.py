from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
    
class LayoutAndStylingTest(FunctionalTest):
    '''тест макета и стилевого оформления'''
    
    def test_layout_and_styling(self):
        '''тест макета и стилевого оформления'''
        # Эдит открывает домашнюю страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # Она замечает, что поле ввода аккуратно центрировано
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width'] / 2,
        512,
        delta=10
        )
        # Она начинает новый список и видит, что поле ввода там тоже
        # аккуратно центировано
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width'] / 2,
        512,
        delta=10)