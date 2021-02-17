import unittest
from webdriver.webdriver import Driver
from paginas.calc import Calc

class TestsCalc(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_somar_numeros(self):
        calc = Calc(self.driver.instance)
        calc.somar([4,2,1])
        sum_py = 4 + 2 + 1
        assert sum_py == calc.obter_resultado(), "Soma esta incorreta!"

    def test_subtrair_numeros(self):
        calc = Calc(self.driver.instance)
        calc.subtrair([4,2,1])
        sub_py = 4 - 2 - 1
        assert sub_py == calc.obter_resultado(), "Subtracao esta incorreta!"

    def test_multiplicar_numeros(self):
        calc = Calc(self.driver.instance)
        calc.multiplicar([4,2,1])
        mult_py = 4 * 2 * 1
        assert mult_py == calc.obter_resultado(), "Multiplicacao esta incorreta!"

    def test_dividir_numeros(self):
        calc = Calc(self.driver.instance)
        calc.dividir([4,2,1])
        div_py = 4 / 2 / 1
        assert div_py == calc.obter_resultado(), "Divisao esta incorreta!"

    def tearDown(self):
        self.driver.instance.quit()
