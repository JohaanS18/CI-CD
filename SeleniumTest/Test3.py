import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_python_org_page_loads(self):
        """Verifica que la página de Python.org cargue correctamente y el título contenga 'Python'"""
        self.driver.get("https://www.python.org")
        self.assertIn("Python", self.driver.title, "El título de la página no contiene 'Python'.")

    def test_search_functionality(self):
        """Verifica que la funcionalidad de búsqueda en Python.org esté operativa"""
        self.driver.get("https://www.python.org")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("unittest")
        search_box.submit()
        self.assertIn("Search Python.org", self.driver.title, "El título de la página de resultados no es el esperado.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()