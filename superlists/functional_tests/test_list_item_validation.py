from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        '''тест: нельзя добавлять пустые элементы списка'''
        # Эдит открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка. Она нажимает Enter на пустом поле ввода
        self.browser.get(self.live_server_url)
        self.browser.find_element('id','id_new_item').send_keys(Keys.ENTER)
        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element('css selector','.has-error').text,
            "You can't have an empty list item"
            ))
        # Она пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        self.browser.find_element('id','id_new_item').send_keys('Buy milk')
        self.browser.find_element('id','id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        # Как ни странно, Эдит решает отправить второй пустой элемент списка
        self.browser.find_element('id','id_new_item').send_keys(Keys.ENTER)
        # Эдит получает аналогичное предупреждение на странице списка
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element('css selector','.has-error').text,
            "You can't have an empty list item"
            ))
        # И она может его исправить, заполнив поле неким текстом
        self.browser.find_element('id','id_new_item').send_keys('Make tea')
        self.browser.find_element('id','id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')