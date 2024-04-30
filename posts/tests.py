from django.test import TestCase, Client, SimpleTestCase
from django.contrib.auth.models import *
from .models import Task
from .views import *
from django.urls import reverse, resolve

# Create your tests here.

#class FirstTestCase(TestCase):

"""def setUp(self):
        print('Setup called')

    def test_equal(self):
        self.assertEqual(1, 1)"""
    
class TestModels(TestCase):
    def setup(self):
        pass

    def test_model_Task(self):
        Task1 = Task.objects.create(
            title="My task"
        )
        self.assertEquals(str(Task1), 'My task')
        self.assertTrue(isinstance(Task1, Task))

class TestViews(TestCase):
        # Client import is use to act as a browser
        def setUp(self):
            self.client = Client()

            # urls
            self.index_url = reverse('list')
            self.task = Task.objects.create(title='Test Task')

        def test_add_task(self):
            response = self.client.post(reverse('list'),{'title': 'Test Task'})
            self.assertEqual(response.status_code, 302)  #302 is the HTTP status code for a redirect
            self.assertEqual(Task.objects.count(), 2)

        def test_index_GET(self):
            # mock the response
            response = self.client.get(self.index_url)
            
            # write asserttion
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "tasks/list.html")

class TestUrls(SimpleTestCase):
     
        def test_list_url_is_resolved(self):
            url = reverse('list')
            print(resolve(url))
            self.assertEquals(resolve(url).func, index)        
