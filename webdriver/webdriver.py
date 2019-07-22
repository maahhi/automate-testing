
from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
          "platformName": "android",
          "deviceName": "7fd02724",
          "appPackage": "taxi.tap30.driver",
          "appActivity": "taxi.tap30.driver.RootActivity"
        }

        self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


