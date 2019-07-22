from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TaxiDriverscreen:
    def __init__(self,driver):
        self.driver = driver
        self.etext_signin_phonenumber = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/edittext_signinphonenumber_number")))
        self.sbutton_signin_phonenumber = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/smartbutton_signinphonenumber")))

    def signin_inter_phone_number(self,phone_number):
        no = str(phone_number)
        self.driver.instance.find_element(MobileBy.ID,"taxi.tap30.driver:id/edittext_signinphonenumber_number").set_value(phone_number)
        print(self.etext_signin_phonenumber.text,phone_number)
        assert "j" in self.etext_signin_phonenumber.text, "Clicked number wasn't reflected."