from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


class Calc():
    def __init__(self, driver):
        self.driver = driver
        self.btPlus = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "plus"
        )))
        self.btMinus = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "minus"
        )))
        self.btMultiply = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "multiply"
        )))
        self.btDivide = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "divide"
        )))
        self.btEquals = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "equals"
        )))

        self.resultado = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                MobileBy.ID, "result"
        )))

    def clicar_numero(self, num):
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, "com.android.calculator2:id/digit_"+str(num)
        )))
        wait.click()


    def somar(self, nums):
        i = 0
        for n in nums:
            if (i > 0):
                self.btPlus.click()
            self.clicar_numero(n)
            i=+1
        self.btEquals.click()

    def subtrair(self, nums):
        i = 0
        for n in nums:
            if (i > 0):
                self.btMinus.click()
            self.clicar_numero(n)
            i=+1
        self.btEquals.click()

    def multiplicar(self, nums):
        i = 0
        for n in nums:
            if (i > 0):
                self.btMultiply.click()
            self.clicar_numero(n)
            i=+1
        self.btEquals.click()

    def dividir(self, nums):
        i = 0
        for n in nums:
            if (i > 0):
                self.btDivide.click()
            self.clicar_numero(n)
            i=+1
        self.btEquals.click()

    def obter_resultado(self):
        return int(self.resultado.text)