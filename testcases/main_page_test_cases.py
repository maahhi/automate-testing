import unittest

from pageobjects.taxi_driver_screen import TaxiDriverscreen
from webdriver.webdriver import Driver

'''
connection error
wrong phone number
wrong verification code


'''

class MainPageTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MainPageTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)


