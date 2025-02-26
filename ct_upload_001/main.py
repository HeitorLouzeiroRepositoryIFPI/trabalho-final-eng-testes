import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestFileUpload(unittest.TestCase):
    def setUp(self):
        """Configuração inicial do caso de teste."""
        print("\n" + "="*50)
        print("Iniciando teste de upload de arquivo...")
        print("="*50)
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://the-internet.herokuapp.com'

        # Criar arquivo temporário para teste
        self.file_path = os.path.join(os.getcwd(), "test_file.txt")
        with open(self.file_path, "w") as f:
            f.write("Teste de upload de arquivo")

    def test_file_upload(self):
        """Teste de upload de arquivo."""
        print("\nExecutando teste de upload de arquivo:")
        print("-"*30)

        # Acessar página de upload
        print("1. Acessando página de upload...")
        self.driver.get(f'{self.base_url}/upload')
        time.sleep(2)

        # Realizar upload
        print("2. Realizando upload do arquivo...")
        file_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "file-upload"))
        )
        file_input.send_keys(self.file_path)
        time.sleep(1)  # Aguarda para visualizar arquivo selecionado

        # Clicar no botão de upload
        print("3. Enviando arquivo...")
        upload_button = self.driver.find_element(By.ID, "file-submit")
        upload_button.click()
        time.sleep(2)  # Aguarda para visualizar progresso

        # Verificar sucesso do upload
        print("4. Verificando resultado do upload...")
        success_text = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        ).text
        self.assertEqual("File Uploaded!", success_text)
        print("   ✓ Arquivo enviado com sucesso!")

        # Verificar nome do arquivo
        uploaded_file = self.driver.find_element(By.ID, "uploaded-files")
        self.assertIn("test_file.txt", uploaded_file.text)
        print("   ✓ Nome do arquivo verificado!")

    def tearDown(self):
        """Limpeza após cada teste."""
        if self.driver:
            print("\nFinalizando teste e fechando navegador...")
            time.sleep(2)
            self.driver.quit()

        # Remover arquivo temporário
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print("Arquivo temporário removido.")

        print("="*50 + "\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
