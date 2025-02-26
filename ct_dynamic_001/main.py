import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestDynamicContent(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de conteúdo dinâmico...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://the-internet.herokuapp.com'

    def test_dynamic_content(self):
        """Teste de conteúdo dinâmico."""
        print("\nExecutando teste de conteúdo dinâmico:")
        print("-"*30)

        # Acessar página de conteúdo dinâmico
        print("1. Acessando página de conteúdo dinâmico...")
        self.driver.get(f'{self.base_url}/dynamic_content')
        time.sleep(2)

        # Capturar conteúdo inicial
        print("2. Capturando conteúdo inicial...")
        initial_content = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "large-10"))
        )
        initial_texts = [elem.text for elem in initial_content]
        print("   ✓ Conteúdo inicial capturado!")
        time.sleep(1)

        # Recarregar página
        print("3. Recarregando página para verificar mudanças...")
        self.driver.refresh()
        time.sleep(2)

        # Capturar novo conteúdo
        print("4. Verificando alterações no conteúdo...")
        new_content = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "large-10"))
        )
        new_texts = [elem.text for elem in new_content]

        # Verificar se houve mudança
        changes_found = False
        print("\nComparando alterações:")
        for i, (old, new) in enumerate(zip(initial_texts, new_texts), 1):
            if old != new:
                changes_found = True
                print(f"   ✓ Mudança detectada no elemento {i}:")
                print(f"      Antes: {old[:50]}...")
                print(f"      Depois: {new[:50]}...")

        self.assertTrue(changes_found, "Nenhuma mudança detectada no conteúdo")
        print("\n>>> Teste de conteúdo dinâmico PASSOU!")

    def test_dynamic_controls(self):
        """Teste de controles dinâmicos."""
        print("\nExecutando teste de controles dinâmicos:")
        print("-"*30)

        # Acessar página de controles dinâmicos
        print("1. Acessando página de controles dinâmicos...")
        self.driver.get(f'{self.base_url}/dynamic_controls')
        time.sleep(2)

        # Testar remoção de checkbox
        print("2. Testando remoção de checkbox...")
        remove_button = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
            )
        )
        remove_button.click()

        # Aguardar e verificar mensagem
        print("3. Verificando resultado da remoção...")
        message = self.wait.until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        self.assertEqual("It's gone!", message.text)
        print("   ✓ Checkbox removido com sucesso!")
        time.sleep(1)

        # Testar habilitação de input
        print("4. Testando habilitação de input...")
        enable_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[onclick='swapInput()']"
        )
        enable_button.click()

        # Aguardar e verificar estado do input
        print("5. Verificando estado do input...")
        input_element = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
        )
        self.assertTrue(input_element.is_enabled())
        print("   ✓ Input habilitado com sucesso!")

        print("\n>>> Teste de controles dinâmicos PASSOU!")

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            time.sleep(2)
            self.driver.quit()
            print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
