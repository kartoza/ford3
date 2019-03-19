
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # noqa
from selenium.common.exceptions import WebDriverException
from django.test import TestCase


class TestProviderForm(TestCase):

    def setUp(self):
        self.browser = webdriver.Remote("http://172.21.0.1:4444/wd/hub",
                                  DesiredCapabilities.CHROME)

    def tearDown(self):
        self.browser.quit()

    def runTest(self):

        # User has created a basic account and now needs to add
        # provider form details and have been redirected to the provider form.

        self.browser.get('http://10.0.0.6:80/ProviderForm/#')
        html = self.browser.page_source
        self.assertTrue(html.startswith('<!DOCTYPE html'))
        self.assertIn('FORD3', self.browser.title)
        # They are greeted with their username
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome, ', header_text)

        # They add their image
        # Chose their provider type

        # They are asked for their tel no.
        inputbox = self.browser.find_element_by_name('provider_tel')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '••• ••• ••••'
        )

        # Which they enter as
        inputbox.send_keys('082 123 3444')

        # They are asked for their email.
        inputbox = self.browser.find_element_by_name('provider_email')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'example@example.com'
        )

        # Enter their Email Address
        inputbox.send_keys('provider_test@fakedomain.com')

        # They submit their data by clicking on the submit button
        submit_button = self.browser.find_element_by_class_name('edu-button')
        submit_button.click()
