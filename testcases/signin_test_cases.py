import unittest

from pageobjects.taxi_driver_screen import TaxiDriverscreen
from webdriver.webdriver import Driver

'''
connection error
wrong phone number
wrong verification code


'''

class SigninTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()


    def test_login(self):

        taxidriver = TaxiDriverscreen(self.driver)
        phone_number = '09998887766'
        taxidriver.signin_inter_phone_number(phone_number)
        taxidriver.signin_click_button()

        taxidriver.verification_page_loaded()

        code = '15937'
        taxidriver.verification_inter_code(code)
        taxidriver.main_page_loaded()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SigninTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)


