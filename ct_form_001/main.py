import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestFormFilling(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de preenchimento de formulário...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://ultimateqa.com/filling-out-forms/')
        time.sleep(2)  # Aguarda 2 segundos para visualizar a página inicial
        self.wait = WebDriverWait(self.driver, 10)

    def test_successful_form_submission(self):
        """Teste de envio de formulário com dados corretos."""
        print("\nExecutando teste de envio correto do formulário:")
        print("-"*30)

        # Localizar campos do formulário
        print("1. Localizando campos do formulário...")
        name = self.wait.until(EC.presence_of_element_located(
            (By.ID, "et_pb_contact_name_0")))
        message = self.driver.find_element(By.ID, "et_pb_contact_message_0")
        time.sleep(1)  # Aguarda 1 segundo após localizar os campos

        # Preencher formulário
        print("2. Preenchendo formulário com dados válidos:")
        print("   - Nome: João Silva")
        name.send_keys("João Silva")
        time.sleep(1)  # Aguarda 1 segundo após preencher o nome

        print("   - Mensagem: Teste de envio de formulário")
        message.send_keys("Teste de envio de formulário")
        time.sleep(1)  # Aguarda 1 segundo após preencher a mensagem

        # Enviar formulário
        print("3. Enviando formulário...")
        submit_button = self.driver.find_element(
            By.NAME, "et_builder_submit_button")
        submit_button.click()
        time.sleep(2)  # Aguarda 2 segundos após enviar o formulário

        # Verificar sucesso
        print("4. Verificando resultado do envio...")
        success_message = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "et-pb-contact-message"))
        )
        self.assertIn("Thanks for contacting us", success_message.text)
        print("   ✓ Mensagem de sucesso encontrada!")
        # Aguarda 2 segundos para visualizar a mensagem de sucesso
        time.sleep(2)
        print("\n>>> Teste de envio correto PASSOU!")

    def test_form_submission_with_missing_data(self):
        """Teste de envio de formulário com dados ausentes."""
        print("\nExecutando teste de envio com dados ausentes:")
        print("-"*30)

        # Verificar presença dos campos do formulário
        print("1. Verificando presença dos campos obrigatórios...")
        print("   - Verificando campo de nome...")
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "et_pb_contact_name_0")))
        time.sleep(1)  # Aguarda 1 segundo após verificar campo de nome

        print("   - Verificando campo de mensagem...")
        self.driver.find_element(By.ID, "et_pb_contact_message_0")
        time.sleep(1)  # Aguarda 1 segundo após verificar campo de mensagem
        print("   ✓ Campos do formulário encontrados!")

        # Enviar formulário sem preencher campos
        print("2. Tentando enviar formulário sem preencher campos...")
        submit_button = self.driver.find_element(
            By.NAME, "et_builder_submit_button")
        submit_button.click()
        time.sleep(2)  # Aguarda 2 segundos após tentar enviar o formulário

        # Verificar mensagens de erro
        print("3. Verificando mensagens de erro...")
        error_message = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "et-pb-contact-message"))
        )

        # Verificar presença das mensagens de erro esperadas
        error_texts = error_message.text.lower()
        expected_texts = [
            "please, fill in the following fields", "name", "message"]

        for text in expected_texts:
            self.assertIn(text.lower(), error_texts)
            print(f"   ✓ Mensagem '{text}' encontrada!")

        # Aguarda 2 segundos para visualizar as mensagens de erro
        time.sleep(2)

        # Verificar se permanecemos na mesma página
        self.assertIn("filling-out-forms", self.driver.current_url)
        print("   ✓ Permaneceu na página do formulário!")
        time.sleep(1)  # Aguarda 1 segundo antes de finalizar
        print("\n>>> Teste de envio com dados ausentes PASSOU!")

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            time.sleep(2)  # Aguarda 2 segundos antes de fechar o navegador
            self.driver.quit()
            print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
