from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnacksTest(SimpleTestCase) : 
    def test_home_page(self): 
        url=reverse('home')
        actual_status_code = self.client.get(url).status_code
        response=200

        self.assertEqual(actual_status_code,response) 


    def test_about_us_page(self): 
        url=reverse('about_us')
        actual_status_code = self.client.get(url).status_code
        response=200

        self.assertEqual(actual_status_code,response)


    def test_template_home(self): 
        url=reverse('home')
        actual_status_code = self.client.get(url)
        response='home.html'

        self.assertTemplateUsed(actual_status_code,response)

    def test_template_about_us(self): 
        url=reverse('about_us')
        actual_status_code = self.client.get(url)
        response='about_us.html'

        self.assertTemplateUsed(actual_status_code,response)
