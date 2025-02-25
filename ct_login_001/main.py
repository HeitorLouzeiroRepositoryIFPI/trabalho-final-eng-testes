import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de autenticação...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.wait = WebDriverWait(self.driver, 10)

    def test_successful_login(self):
        """Teste de login bem-sucedido com credenciais válidas."""
        print("\nExecutando teste de login bem-sucedido:")
        print("-"*30)

        # Localizar campos de usuário e senha
        print("1. Localizando campos de entrada...")
        username = self.wait.until(
            EC.presence_of_element_located((By.ID, "username")))
        password = self.driver.find_element(By.ID, "password")

        # Inserir credenciais válidas
        print("2. Inserindo credenciais válidas:")
        print("   - Usuário: tomsmith")
        print("   - Senha: SuperSecretPassword!")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")

        # Clicar no botão de login
        print("3. Clicando no botão de login...")
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Verificar login bem-sucedido
        print("4. Verificando resultado do login...")
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
        )
        self.assertIn("You logged into a secure area!", success_message.text)
        print("   ✓ Mensagem de sucesso encontrada!")

        # Verificar se estamos na página segura
        self.assertIn("/secure", self.driver.current_url)
        print("   ✓ Redirecionado para área segura!")
        print("\n>>> Teste de login bem-sucedido PASSOU!")

    def test_failed_login(self):
        """Teste de login com falha usando credenciais inválidas."""
        print("\nExecutando teste de login com falha:")
        print("-"*30)

        # Localizar campos de usuário e senha
        print("1. Localizando campos de entrada...")
        username = self.wait.until(
            EC.presence_of_element_located((By.ID, "username")))
        password = self.driver.find_element(By.ID, "password")

        # Inserir credenciais inválidas
        print("2. Inserindo credenciais inválidas:")
        print("   - Usuário: invalid_user")
        print("   - Senha: invalid_password")
        username.send_keys("invalid_user")
        password.send_keys("invalid_password")

        # Clicar no botão de login
        print("3. Clicando no botão de login...")
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Verificar mensagem de erro
        print("4. Verificando resultado do login...")
        error_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "flash.error"))
        )
        self.assertIn("Your username is invalid!", error_message.text)
        print("   ✓ Mensagem de erro encontrada!")

        # Verificar se permanecemos na página de login
        self.assertIn("/login", self.driver.current_url)
        print("   ✓ Permaneceu na página de login!")
        print("\n>>> Teste de login com falha PASSOU!")

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            self.driver.quit()
            print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
