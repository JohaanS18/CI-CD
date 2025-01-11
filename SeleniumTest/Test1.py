import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCampusVirtual(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_load_page_and_verify_title(self):
        """Comprueba que el título de la página principal coincida con el esperado"""
        self.driver.get("https://campusvirtualunillanos.co/")
        actual_title = self.driver.title
        expected_title = "Página Principal | Campus Virtual"
        self.assertTrue(expected_title in actual_title, "El título de la página no es correcto.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
