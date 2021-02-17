# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class Driver:
    def __init__(self):

        caps = {
                    "platformName":"Android",
                    "deviceName":"emulator-5554",
                    "appPackage":"com.android.calculator2",
                    "appActivity":"com.android.calculator2.Calculator",
                    "ensureWebviewsHavePages":True
                }
        # Driver
        self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)