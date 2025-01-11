import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GooglePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_page_loads(self):
        """Verifica que la página de Google cargue correctamente y que el título contenga 'Google'"""
        self.driver.get("https://www.google.com.co")
        self.assertIn("Google", self.driver.title, "El título de la página no contiene 'Google'.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
