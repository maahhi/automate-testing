from appium.webdriver.common.mobileby import MobileBy,By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TaxiDriverscreen:
    def __init__(self,driver):
        self.driver = driver
        self.etext_signin_phone_number = WebDriverWait(self.driver.instance, 3).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/edittext_signinphonenumber_number")))
        self.sbutton_signin_phone_number = WebDriverWait(self.driver.instance, 3).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/smartbutton_signinphonenumber")))

    def verification_page_loaded(self):
        self.sbutton_signin_verificationcode = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/smartbutton_signinverificationcode")))
        etexr_verification_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText"
        self.etext_verification_list = [
            WebDriverWait(self.driver.instance, 5).until(
                EC.visibility_of_element_located((
                    MobileBy.XPATH, etexr_verification_xpath+"["+str(i)+"]"))) for i in range(1,6)
        ]

    def signin_inter_phone_number(self,phone_number):
        self.etext_signin_phone_number.clear()
        self.etext_signin_phone_number.set_value(phone_number)
        print("phone number",phone_number)
        assert phone_number == self.etext_signin_phone_number.text, "insert phone number wasn't reflected."

    def signin_clear_phone_number(self):
        self.etext_signin_phone_number.clear()
        assert "" == self.etext_signin_phone_number.text, "insert phone number wasn't reflected."

    def signin_click_button(self):
        self.sbutton_signin_phone_number.click()

    def verification_inter_code(self,code):
        #self.etext_signin_verificationcode.clear()
        for i in range(5):
            etext = self.etext_verification_list[i]
            etext.set_value(code[i])
        #self.etext_signin_verificationcode.set_value(code)
        '''
        etext_signin_verificationcode = ""
        for i in range(5):
            etext_signin_verificationcode += self.etext_verification_list[i].text

        print("code",etext_signin_verificationcode)
        assert code == etext_signin_verificationcode , "insert verification code wasn't reflected."
        '''


    def main_page_loaded(self):
        self.button_online_offline = WebDriverWait(self.driver.instance, 3).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "taxi.tap30.driver:id/toggle_bg")))



