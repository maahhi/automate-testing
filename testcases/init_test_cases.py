import unittest

from pageobjects.taxi_driver_screen import TaxiDriverscreen
from webdriver.webdriver import Driver


class InitTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()


    def test_login(self):

        taxidriver = TaxiDriverscreen(self.driver)
        phone_number = '09998887766'
        taxidriver.signin_inter_phone_number(phone_number)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InitTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)


