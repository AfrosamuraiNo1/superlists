from django.test import TestCase
from lists.models import Item, List
from django.utils.html import escape

class HomePageTest(TestCase):
    '''тест домашней страницы'''
    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

class NewListTest(TestCase):
    '''тест нового списка'''
    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
    
    def test_redirects_after_POST(self):
        '''тест: переадресует после post-запроса'''
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')
    
    def test_validation_errors_are_sent_back_to_home_page_template(self):
        '''тест: ошибки валидации отсылаются назад в шаблон
        домашней страницы'''
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)
    
    def test_invalid_list_items_arent_saved(self):
        '''тест: сохраняются недопустимые элементы списка'''
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

# class NewItemTest(TestCase):
#     '''тест нового элемента списка'''
#     def test_can_save_a_POST_request_to_an_existing_list(self):
#         '''тест: можно сохранить post-запрос в существующий список'''
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#         self.client.post(f'/lists/{correct_list.id}/add_item',data={'item_text': 'A new item for an existing list'})
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new item for an existing list')
#         self.assertEqual(new_item.list, correct_list)
    
    # def test_redirects_to_list_view(self):
    #     '''тест: переадресуется в представление списка'''
    #     other_list = List.objects.create()
    #     correct_list = List.objects.create()
    #     response = self.client.post(f'/lists/{correct_list.id}/add_item',data={'item_text': 'A new item for an existing list'})
    #     self.assertRedirects(response, f'/lists/{correct_list.id}/')

class ListViewTest(TestCase):
    '''тест представления списка'''

    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_passes_correct_list_to_template(self):
        '''тест: передается правильный список в шаблон'''
    [...]
    def test_displays_only_items_for_that_list(self):
        '''тест: отображаются элементы только для этого списка'''
    [...]
    def test_can_save_a_POST_request_to_an_existing_list(self):
        '''тест: можно сохранить post-запрос в существующий список'''
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(f'/lists/{correct_list.id}/',data={'item_text': 'A new item for an existing list'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)
    
    def test_POST_redirects_to_list_view(self):
        '''тест: post-запрос переадресуется в представление списка'''
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(f'/lists/{correct_list.id}/',data={'item_text': 'A new item for an existing list'})
        self.assertRedirects(response, f'/lists/{correct_list.id}/')