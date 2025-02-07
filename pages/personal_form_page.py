from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from utils.helpers import generar_identificacion_aleatoria
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas


class PersonalFormPage(BasePage):
    def personal_form(self):
        self.enter_text(By.XPATH, "//input[@data-id='date-picker-slds-input']", '12/28/1984') # Ingresar la fecha en el campo de fecha usando el input de tipo date
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-351"]')  # Encuentra el combobox (desplegable) para seleccionar un valor.
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el combobox a la vista.
        dropdown.click()  # Hace clic en el combobox para mostrar las opciones.
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        option_xpath = f'//div[@role="option" and @data-value="Masculino"]'  # XPath para la opción "Masculino" en el dropdown.
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))  # Espera hasta que la opción esté clickeable.
        time.sleep(2)  # Pausa de 2 segundos para garantizar la interacción completa.
        option.click()  # Hace clic en la opción "Masculino".
        radio = self.wait_for_element(By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")  # Espera hasta que el radio button sea visible.
        self.driver.execute_script("arguments[0].click();", radio)  # Usa Javascript para hacer clic en el radio button.
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-376"]')  # Encuentra el dropdown.
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el dropdown a la vista si es necesario.
        dropdown.click()  # Hace clic para desplegar las opciones del dropdown.
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        one_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="01"]]')))  # Espera hasta que la opción "01" sea clickeable.
        one_option.click()  # Hace clic en la opción "01".
        time.sleep(2)  # Pausa de 2 segundos para garantizar que la acción se complete.
        self.enter_text(By.XPATH, '//*[@id="input41-384"]', config.NOMBRED)  # Ingresa el nombre en el campo correspondiente.
        self.enter_text(By.XPATH, '//*[@id="input43-386"]', config.PAPELLIDOD)  # Ingresa el primer apellido en el campo correspondiente.
        self.enter_text(By.XPATH, '//*[@id="input45-388"]', config.SAPELLIDOD)  # Ingresa el segundo apellido en el campo correspondiente.
        self.select_dropdown_option(
            (By.XPATH, '//*[@id="comboboxId-390"]'),
            (By.XPATH, '//div[@role="option" and .//span[text()="Hijo/a"]]')
        )
        date_input = self.driver.find_element(By.XPATH, '//*[@id="date-input-394"]')  # Encuentra el campo de fecha.
        date_input.send_keys('01/18/1970')  # Ingresa la fecha manualmente (por ejemplo, 01/18/1970).
        time.sleep(8)  # Espera 8 segundos para asegurar que la fecha se haya ingresado correctamente.
        date_input.click()  # Hace clic en el campo para completar la interacción.
        save_button = self.wait_for_element(By.XPATH, '//button[contains(text(), "Guardar y continuar")]')  # Espera hasta que el botón esté visible.
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)  # Desplaza el dropdown a la vista si es necesario.
        # Desplaza el botón a la vista si no está visible.
        save_button.click()  # Hace clic en el botón para continuar.
        time.sleep(5)  # Espera 5 segundos para asegurar que la acción se haya completado.
        print("Validación Información Personal")
        pass