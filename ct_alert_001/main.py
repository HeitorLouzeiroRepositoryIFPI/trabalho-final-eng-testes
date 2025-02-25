import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAlerts(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de alertas e pop-ups...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        time.sleep(2)  # Aguarda 2 segundos para visualizar a página inicial
        self.wait = WebDriverWait(self.driver, 10)

    def test_confirm_alert(self):
        """Teste de confirmação de alerta JavaScript."""
        print("\nExecutando teste de confirmação de alerta:")
        print("-"*30)

        # Localizar e clicar no botão que gera o alerta de confirmação
        print("1. Localizando botão de alerta de confirmação...")
        xpath = "//button[contains(text(), 'Click for JS Confirm')]"
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print("2. Clicando no botão para gerar alerta...")
        confirm_button.click()
        time.sleep(2)  # Aguarda para visualizar o alerta

        # Aceitar o alerta
        print("3. Aceitando o alerta...")
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)  # Aguarda para visualizar o resultado

        # Verificar a mensagem de resultado
        print("4. Verificando resultado...")
        result = self.driver.find_element(By.ID, "result")
        self.assertIn("You clicked: Ok", result.text)
        print("   ✓ Confirmação do alerta bem-sucedida!")
        print("\n>>> Teste de confirmação de alerta PASSOU!")
        time.sleep(2)  # Aguarda para visualizar o resultado final

    def test_prompt_alert(self):
        """Teste de captura de prompt JavaScript."""
        print("\nExecutando teste de prompt:")
        print("-"*30)

        # Localizar e clicar no botão que gera o prompt
        print("1. Localizando botão de prompt...")
        xpath = "//button[contains(text(), 'Click for JS Prompt')]"
        prompt_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print("2. Clicando no botão para gerar prompt...")
        prompt_button.click()
        time.sleep(2)  # Aguarda para visualizar o prompt

        # Interagir com o prompt
        print("3. Interagindo com o prompt...")
        alert = self.driver.switch_to.alert
        test_text = "Teste Automatizado"
        print(f"   - Inserindo texto: '{test_text}'")
        alert.send_keys(test_text)
        time.sleep(2)  # Aguarda para visualizar o texto inserido

        print("4. Confirmando o prompt...")
        alert.accept()
        time.sleep(2)  # Aguarda para visualizar o resultado

        # Verificar a mensagem de resultado
        print("5. Verificando resultado...")
        result = self.driver.find_element(By.ID, "result")
        expected_text = f"You entered: {test_text}"
        self.assertEqual(expected_text, result.text)
        print("   ✓ Texto do prompt capturado corretamente!")
        print("\n>>> Teste de prompt PASSOU!")
        time.sleep(2)  # Aguarda para visualizar o resultado final

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            time.sleep(2)  # Aguarda 2 segundos antes de fechar o navegador
            self.driver.quit()
            print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
