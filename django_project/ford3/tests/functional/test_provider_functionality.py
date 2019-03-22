
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # noqa
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

        self.browser.get('http://192.168.43.124:80/ProviderForm/#')
        html = self.browser.page_source
        self.assertTrue(html.startswith('<!DOCTYPE html'))
        self.assertIn('FORD3', self.browser.title)
        # They are greeted with their username
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome, ', header_text)

        # They add their image
        # Chose their provider type

        # They are asked for their tel no.
        inputbox = self.browser.find_element_by_name('telephone')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Primary Contact Number'
        )

        # Which they enter as
        inputbox.send_keys('0821233444')

        # They are asked for their admission no.
        inputbox = self.browser.find_element_by_name('admissions_contact_no')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Admissions contact number'
        )

        # Which they enter as
        inputbox.send_keys('0137441422')

        # They are asked for their admission no.
        inputbox = self.browser.find_element_by_name('physical_address_line_1')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Address Line 1'
        )

        # Which they enter as
        inputbox.send_keys('SomeStreet 28')

        # They are asked for their admission no.
        inputbox = self.browser.find_element_by_name('physical_address_line_2')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Address Line 1'
        )

        # Which they enter as
        inputbox.send_keys('Extension 9')

        # They are asked for their admission no.
        inputbox = self.browser.find_element_by_name('physical_address_city')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'City'
        )

        # Which they enter as
        inputbox.send_keys('Nelspruit')

        # They are asked for their admission no.
        inputbox = self.browser.find_element_by_name('postal_address')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Postal/ZIP Code'
        )

        # Which they enter as
        inputbox.send_keys('1200')



        # They are asked for their email.
        inputbox = self.browser.find_element_by_name('email')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'example@example.com'
        )

        # Enter their Email Address
        inputbox.send_keys('provider_test@fakedomain.com')




        # They submit their data by clicking on the submit button
        submit_button = self.browser.find_element_by_class_name('edu-button')
        submit_button.click()

        # Since they entered too many digits the form returns an error message
