# Conteúdo do test_drag_drop.py será movido para cá
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de drag and drop...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://the-internet.herokuapp.com'

    def test_drag_and_drop(self):
        """Teste de funcionalidade drag and drop."""
        print("\nExecutando teste de drag and drop:")
        print("-"*30)

        # Acessar página de drag and drop
        print("1. Acessando página de drag and drop...")
        self.driver.get(f'{self.base_url}/drag_and_drop')
        time.sleep(2)

        # Localizar elementos
        print("2. Localizando elementos A e B...")
        element_a = self.wait.until(
            EC.presence_of_element_located((By.ID, "column-a"))
        )
        element_b = self.driver.find_element(By.ID, "column-b")

        # Realizar drag and drop
        print("3. Realizando operação de drag and drop...")
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element_a, element_b).perform()
        time.sleep(2)

        # Verificar resultado
        print("4. Verificando resultado...")
        new_position_a = element_a.get_attribute("innerHTML")
        self.assertIn("B", new_position_a)
        print("   ✓ Elementos trocados com sucesso!")

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            time.sleep(2)
            self.driver.quit()
            print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
