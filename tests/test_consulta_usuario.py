from concurrent.futures import wait
import pytest # Framework de pruebas en Python
from selenium import webdriver # Controlador web para automatización de navegadores
from selenium.webdriver.chrome.options import Options # Opciones de configuración para Chrome
from selenium.webdriver.chrome.service import Service # Servicio para administrar el WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By # Permite localizar elementos en la página
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas
from webdriver_manager.chrome import ChromeDriverManager # Administra automáticamente el controlador de Chrome
import time # Manejo de pausas en la ejecución de pruebas
import random
from selenium.common.exceptions import TimeoutException

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
    options.add_argument("--disable-gpu")  # Desactiva el uso de la GPU en el navegador
    driver = webdriver.Chrome(service=service, options=options)
    yield driver  # Devuelve 'driver' y pausa la función hasta que termine su uso.
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
        self.enter_text(driver, By.XPATH, '//*[@id="input17-280"]', config.PAPELLIDO)

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

        # Selección de la ciudad (con una espera explícita)
        dropdown_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='BOGOTA']")
            )
        )
        ActionChains(driver).move_to_element(dropdown_option).perform()  # Desplazarse al elemento
        dropdown_option.click()  # Selección de la opción
        

        # validar que el departamento y el pais son los correctos
        hidden_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input25-296"]')))
        hidden_value = hidden_field.get_attribute(config.DEPARTAMENTO)  # Obtener valor de un campo oculto

        country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input27-298"]')))
        country_value = country_field.get_attribute(config.PAIS)  # Obtener valor de país

        # Ingreso de teléfono
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input33-304"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_field)  # Desplazar a la vista
        driver.execute_script("arguments[0].click();", input_field)  # Hacer clic
        ActionChains(driver).move_to_element(input_field).click().send_keys(config.TELEFONO).perform()

        # Datos del evento
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-307"]', config.EVENTO)

        # Selección del evento (esperar la opción visible y hacer clic)
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
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)  # Desplazar a la vista
        ActionChains(driver).move_to_element(checkbox).click().perform()

        # Hacer clic en el botón de siguiente
        batons = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc/slot/c-global-onboarding-custom-button-cmp/div/button'))
        )
        batons.click()  # Hacer clic en el botón
        print("registro datos de contacto")
        time.sleep(15)


    def personal_form(self, driver):
        # Ingresar la fecha en el campo de fecha usando el input de tipo date
        self.enter_text(driver, By.XPATH, "//input[@data-id='date-picker-slds-input']", '12/28/1984')

        # Seleccionar opción en un combobox (desplegable) para seleccionar un valor
        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-351"]')
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        dropdown.click()

        wait = WebDriverWait(driver, 10)
        option_xpath = f'//div[@role="option" and @data-value="Masculino"]'
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        time.sleep(2)
        option.click()

        # Hacer clic en la opción deseada (un radio button con un valor específico)
        radio = self.wait_for_element(driver, By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")
        driver.execute_script("arguments[0].click();", radio)  # Usar Javascript para hacer clic en el radio button

        # Hacer clic en un dropdown específico, ubicado por su XPath
        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-376"]')
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplazar el dropdown a la vista si es necesario
        dropdown.click()  # Hacer clic para desplegar las opciones

        # Esperar hasta que una opción específica en el dropdown sea clickeable
        wait = WebDriverWait(driver, 10)
        one_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="01"]]')))
        one_option.click()  # Hacer clic en la opción "01"
        time.sleep(2)

        # Ingresar texto en varios campos de texto del formulario (nombre, apellido, etc.)
        self.enter_text(driver, By.XPATH, '//*[@id="input41-384"]', config.NOMBRED)
        self.enter_text(driver, By.XPATH, '//*[@id="input43-386"]', config.PAPELLIDOD)
        self.enter_text(driver, By.XPATH, '//*[@id="input45-388"]', config.SAPELLIDOD)

        # Seleccionar una opción del combobox para el campo "Hijo/a"
        self.select_dropdown_option(driver, '//*[@id="comboboxId-390"]', '//div[@role="option" and .//span[text()="Hijo/a"]]')

        # Ingresar la fecha de nacimiento en el campo correspondiente
        date_input = driver.find_element(By.XPATH,'//*[@id="date-input-394"]')
        # Ingresa la fecha manualmente (por ejemplo, 01/18/1970
        date_input.send_keys('01/18/1970')
        time.sleep(8)
        # Hacer clic en el elemento
        date_input.click()# Esperar 8 segundos para asegurar que la fecha se haya ingresado correctamente
    
        # Hacer clic en el botón "Guardar y continuar"
        save_button = self.wait_for_element(driver, By.XPATH, '//button[contains(text(), "Guardar y continuar")]')
        self.scroll_into_view(driver, save_button)  # Desplazar el botón a la vista si no está visible
        save_button.click()  # Hacer clic en el botón para continuar
        time.sleep(5)
        pass

        #Ingresar perfil financiero
    def perfil_financiero(self, driver):
        # Esperar a que el combobox esté presente
        wait = WebDriverWait(driver, 30)
        elements = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
        print(f"Elementos encontrados: {len(elements)}")
        if not elements:
            raise Exception("El elemento no fue encontrado en la página")

        # Esperar hasta que el combobox sea visible y hacer clic
        question_label = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))
        question_label.click()
        question_label.send_keys("0 a 4.000.000")

        # Selección de la opción en el desplegable (espera explícita)
        dropdown_option = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='0 a 4.000.000']")
        ))

        # Desplazarse al elemento antes de hacer clic
        ActionChains(driver).move_to_element(dropdown_option).perform()
        dropdown_option.click()  # Selección de la opción
        time.sleep(2)
        # Cerrar el navegador después de la ejecución
        question_emple = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[2]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"))
        )
        question_emple.click()
        question_emple.send_keys("Empleado")

        # Esperar a que la opción aparezca en el desplegable y seleccionarla
        option_emple = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='Empleado']")
            )
        )
        ActionChains(driver).move_to_element(option_emple).perform()  # Desplazarse al elemento
        option_emple.click()  # Seleccionar la opción# Ejecución del Test
        currency_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-currency[1]/slot[1]/c-masked-input[1]/div[1]/div[2]/input[1]"))
        )
        currency_input.click()  # Hacer clic en el campo
        currency_input.send_keys("1000000")  # Ingresar el valor 1.000.000
        time.sleep(2)

        checkbox_xpaths = [
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/span[1]",
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[4]/label[1]/span[1]",
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[6]/label[1]/span[1]"
        ]

        # Recorrer la lista y seleccionar cada checkbox con scroll automático
        for xpath in checkbox_xpaths:
            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            
            # Hacer scroll hasta el checkbox
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)

            # Alternativa: Simular flechas de teclado para garantizar el desplazamiento
            ActionChains(driver).move_to_element(checkbox).perform()

            # Esperar a que el checkbox sea clickeable y hacer clic
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        image_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[2]/slot[1]/c-checkbox-image-group[1]/div[1]/div[1]/fieldset[1]/div[1]/div[2]/label[1]/div[1]"

        # Esperar a que la imagen esté presente
        image_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))

        # Hacer scroll hasta la imagen
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", image_element)

        # Esperar a que la imagen sea clickeable y hacer clic
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, image_xpath))).click()

        # XPath del botón a hacer clic
        button_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-custom-lwc[1]/slot[1]/c-global-onboarding-custom-button-cmp[1]/div[1]/button[2]"

        # Esperar a que el botón esté presente en el DOM
        button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))

        # Hacer scroll hasta el botón para asegurarnos de que sea visible
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_element)

        # Esperar a que el botón sea clickeable y hacer clic
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()
        time.sleep(20)
        pass


def test_consulta(driver: WebDriver):
    test = TestConsulta()
    test.login(driver, config.USERNAME, config.PASSWORD)
    test.complete_form(driver)
    test.validate_second_form(driver)
    test.personal_form (driver)
    test.perfil_financiero (driver)