import pytest # Framework de pruebas en Python
from selenium import webdriver # Controlador web para automatización de navegadores
from selenium.webdriver.chrome.options import Options # Opciones de configuración para Chrome
from selenium.webdriver.chrome.service import Service # Servicio para administrar el WebDriver
from selenium.webdriver.common.by import By # Permite localizar elementos en la página
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas
from webdriver_manager.chrome import ChromeDriverManager # Administra automáticamente el controlador de Chrome
import time # Manejo de pausas en la ejecución de pruebas
import random

from config import config # Librería para generar valores aleatorios

def generar_identificacion_aleatoria():
    #Genera un número de identificación aleatorio de 8 dígitos
    return str(random.randint(10000000, 99999999))  # Número aleatorio entre 10000000 y 99999999

@pytest.fixture
def driver():
    # Fixture de pytest para configurar y retornar un WebDriver de Chrome.
    # Se encarga de inicializar el navegador antes de la prueba y cerrarlo después de su ejecución.
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

class TestConsulta:
    def open_url(self, driver, url):
        #Navega a la URL especificada#
        driver.get(url)
        driver.maximize_window()

    def wait_for_element(self, driver, by, value, timeout=10):
        #Espera hasta que un elemento esté presente en la página
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, driver, by, value, timeout=10):
        #Espera a que un elemento sea clickeable y luego hace clic en él
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def enter_text(self, driver, by, value, text):
        #Introduce texto en un campo
        element = self.wait_for_element(driver, by, value)
        element.clear()
        element.send_keys(text)

    def select_dropdown_option(self, driver, dropdown_xpath, option_xpath):
        #Selecciona una opción de un combobox
        self.click_element(driver, By.XPATH, dropdown_xpath)
        self.click_element(driver, By.XPATH, option_xpath)

    def scroll_into_view(self, driver, element):
        #Desplaza la página hasta que un elemento sea visible
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def login(self, driver, username, password):
        #Inicia sesión en Salesforce
        self.open_url(driver, "https://globalseguros--qaonb.sandbox.my.salesforce.com/")
        self.enter_text(driver, By.CSS_SELECTOR, "input[name='username']", username)
        self.enter_text(driver, By.ID, 'password', password)
        self.click_element(driver, By.CSS_SELECTOR, "input[id='Login']")
        time.sleep(15)
        print("Ingreso Login")

    def complete_form(self, driver):
        #Completa el formulario de la página de destino
        target_url = "https://globalseguros--qaonb.sandbox.lightning.force.com/lightning/cmp/vlocity_ins__vlocityLWCOmniWrapper?c__target=c%3AgsvFormularyEnglish&c__layout=lightning&c__tabLabel=Perfilamiento"
        self.open_url(driver, target_url)

        # Seleccionar opción en combobox
        self.select_dropdown_option(driver, '//*[@id="comboboxId-211"]', '//div[@role="option" and .//span[text()="CEDULA DE CIUDADANIA"]]')
        # Genera un número de identificación aleatorio de 8 dígitos
        numero_identificacion = generar_identificacion_aleatoria()
        # Ingresa el número de identificación generado en el campo correspondiente
        self.enter_text(driver, By.XPATH, '//*[@id="input1-214"]', numero_identificacion)
        # Ingresa el texto "PARTNER ComLog OnBO1" en otro campo de entrada
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-227"]', config.ASESOR)
        # Espera hasta que la opción específica del dropdown esté disponible en la página
        dropdown_option = self.wait_for_element(driver, By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and contains(text(), 'PROYECTA-T LTDA-BOGOTA')]")
        # Mueve el cursor hasta la opción del dropdown para asegurar que sea visible e interactuable
        ActionChains(driver).move_to_element(dropdown_option).perform()
        # Hace clic en la opción para seleccionarla
        dropdown_option.click()
        # Hacer clic en 'Siguiente'
        next_button = self.wait_for_element(driver, By.XPATH, "//button[.//span[text()='Siguiente']]")
        # Desplaza la página hasta que el botón "Next" sea visible en la pantalla
        self.scroll_into_view(driver, next_button)
        # Hace clic en el botón "Next" para continuar con el proceso
        next_button.click()
        # Imprime un mensaje en la consola indicando que se realizó la validación del tomador
        print("Validación de tomador")

    def validate_second_form(self, driver):
        # Valida y completa el segundo formulario en el proceso de automatización.
        # Args: driver (webdriver): Instancia del navegador en uso.
        wait = WebDriverWait(driver, 10)
        # Ingreso de datos en el formulario de los Nombres
        self.enter_text(driver, By.XPATH, '//*[@id="input15-278"]', config.NOMBRE)
        # Ingreso de datos en el formulario del Primer Apellido
        self.enter_text(driver, By.XPATH, '//*[@id="input17-280"]',config.PAPELLIDO )
        # Ingreso de datos en el formulario del Segundo Apellido
        self.enter_text(driver, By.XPATH, '//*[@id="input19-282"]', config.SAPELLIDO)
        # Ingreso de correo electrónico
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input23-289"]')))
        email_field.clear()
        email_field.send_keys(config.EMAIL)
        # Verificar el valor ingresado
        entered_email = email_field.get_attribute("value")
        print(f"Email ingresado: {entered_email}")
        # Datos de la ciudad
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-292"]', config.CIUDAD)
        # Selección de la ciudad
        dropdown_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='BOGOTA']")
            )
        )
        ActionChains(driver).move_to_element(dropdown_option).perform()
        dropdown_option.click()
        # Esperar y obtener valor de un campo oculto
        hidden_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input25-296"]')))
        hidden_value = hidden_field.get_attribute(config.DEPARTAMENTO)
        country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input27-298"]')))
        country_value = country_field.get_attribute(config.PAIS)

        # Ingreso de teléfono
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input33-304"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_field)
        driver.execute_script("arguments[0].click();", input_field)
        ActionChains(driver).move_to_element(input_field).click().send_keys(config.TELEFONO).perform()

        # Datos del evento
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-307"]', config.EVENTO)

        # Selección del evento
        dropdown_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='FERIA DEL LIBRO 2024']")
            )
        )
        ActionChains(driver).move_to_element(dropdown_option).perform()
        dropdown_option.click()

        # Marcar checkbox
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-checkbox_faux"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        ActionChains(driver).move_to_element(checkbox).click().perform()

        # Hacer clic en el botón de siguiente
        batons = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc/slot/c-global-onboarding-custom-button-cmp/div/button'))
        )
        batons.click()
        print("registro datos de contacto")
        time.sleep(15)

    def personal_form(self, driver):

        date_input = driver.find_element(By.XPATH, "//input[@data-id='date-picker-slds-input']")
        date_input.send_keys('12/28/1984')
        # Seleccionar opción en combobox
        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-351"]')
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        dropdown.click()

        # Esperar a que aparezcan las opciones en la lista desplegable
        wait = WebDriverWait(driver, 10)
        option_xpath = f'//div[@role="option" and @data-value="Masculino"]'
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        time.sleep(2)

        # Hacer clic en la opción deseada
        option.click()
        # Encuentra el radio button usando el selector de clase
        radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")
        driver.execute_script("arguments[0].click();", radio)

        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-376"]')
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        dropdown.click()

        # Esperar a que la opción "-- Clear --" esté visible y sea clickeable
        wait = WebDriverWait(driver, 10)
        none_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="Ninguna"]]')))
        none_option.click()
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Guardar y continuar")]')))
        # Hacer scroll hasta el botón (opcional, si está fuera de la vista)
        driver.execute_script("arguments[0].scrollIntoView();", save_button)
        # Hacer clic en el botón
        save_button.click()

        time.sleep(15)

        # Llamada a la función con el valor "Masculino" o "Femenino"
        pass

# Ejecución del Test
def test_consulta(driver):
    test = TestConsulta()
    test.login(driver, config.USERNAME, config.PASSWORD)
    test.complete_form(driver)
    test.validate_second_form(driver)
    test.personal_form (driver)






