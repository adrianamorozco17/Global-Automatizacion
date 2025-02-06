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
        driver.get(url) #Navega a la URL especificada#
        driver.maximize_window()# Maximiza la ventana del navegador

    def wait_for_element(self, driver, by, value, timeout=10): 
        #Espera hasta que un elemento esté presente en la página
        return WebDriverWait(driver, timeout).until( # Espera hasta que el elemento esté presente en el DOM de la página según el localizador (by, value).
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, driver, by, value, timeout=10): 
        #Espera a que un elemento sea clickeable y luego hace clic en él
        element = WebDriverWait(driver, timeout).until(  # Espera hasta que el elemento esté disponible para hacer clic (es decir, esté visible y habilitado).
            EC.element_to_be_clickable((by, value))
        )
        element.click()  # Realiza un clic en el elemento una vez que esté disponible y listo para ser interactuado.

    def enter_text(self, driver, by, value, text):     
        # Introduce texto en un campo de entrada una vez que el elemento esté presente y accesible.
        element = self.wait_for_element(driver, by, value)
        element.clear()  # Limpia cualquier texto previamente ingresado en el campo.
        element.send_keys(text)  # Escribe el texto proporcionado en el campo.

    def select_dropdown_option(self, driver, dropdown_xpath, option_xpath): 
        # Selecciona una opción de un combobox haciendo clic en el dropdown y luego en la opción deseada.
        self.click_element(driver, By.XPATH, dropdown_xpath)
        self.click_element(driver, By.XPATH, option_xpath)

    def scroll_into_view(self, driver, element):
        # Desplaza la página hasta que el elemento especificado sea visible en la vista.
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def login(self, driver, username, password):
        # Inicia sesión en Salesforce con las credenciales proporcionadas.
        self.open_url(driver, "https://globalseguros--qaonb.sandbox.my.salesforce.com/")
        self.enter_text(driver, By.CSS_SELECTOR, "input[name='username']", username)
        self.enter_text(driver, By.ID, 'password', password)
        self.click_element(driver, By.CSS_SELECTOR, "input[id='Login']")
        time.sleep(15)  # Espera para garantizar que el inicio de sesión se complete antes de continuar.
        print("Ingreso Login")

    def complete_form(self, driver):
        #Completa el formulario de la página de destino
        target_url = "https://globalseguros--qaonb.sandbox.lightning.force.com/lightning/cmp/vlocity_ins__vlocityLWCOmniWrapper?c__target=c%3AgsvFormularyEnglish&c__layout=lightning&c__tabLabel=Perfilamiento"
        self.open_url(driver, target_url) # Seleccionar opción en combobox
        self.select_dropdown_option(driver, '//*[@id="comboboxId-211"]', '//div[@role="option" and .//span[text()="CEDULA DE CIUDADANIA"]]')
        # Genera un número de identificación aleatorio de 8 dígitos
        numero_identificacion = generar_identificacion_aleatoria() # Ingresa el número de identificación generado en el campo correspondiente
        self.enter_text(driver, By.XPATH, '//*[@id="input1-214"]', numero_identificacion) # Ingresa el texto "PARTNER ComLog OnBO1" en otro campo de entrada
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-227"]', config.ASESOR) # Espera hasta que la opción específica del dropdown esté disponible en la página
        dropdown_option = self.wait_for_element(driver, By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and contains(text(), 'PROYECTA-T LTDA-BOGOTA')]")
        # Mueve el cursor hasta la opción del dropdown para asegurar que sea visible e interactuable
        ActionChains(driver).move_to_element(dropdown_option).perform() # Hace clic en la opción para seleccionarla
        dropdown_option.click() # Hacer clic en 'Siguiente'
        next_button = self.wait_for_element(driver, By.XPATH, "//button[.//span[text()='Siguiente']]") # Desplaza la página hasta que el botón "Next" sea visible en la pantalla
        self.scroll_into_view(driver, next_button) # Hace clic en el botón "Next" para continuar con el proceso
        next_button.click() # Imprime un mensaje en la consola indicando que se realizó la validación del tomador
        print("Validación de tomador")

    def validate_second_form(self, driver):
        # Valida y completa el segundo formulario en el proceso de automatización.
        # Args: driver (webdriver): Instancia del navegador en uso.
        wait = WebDriverWait(driver, 10)  # Espera explícita hasta que el formulario esté listo para ser validado.
        self.enter_text(driver, By.XPATH, '//*[@id="input15-278"]', config.NOMBRE) # Ingreso de datos en el formulario de los Nombres
        self.enter_text(driver, By.XPATH, '//*[@id="input17-280"]', config.PAPELLIDO) # Ingreso de datos en el formulario del Primer Apellido
        self.enter_text(driver, By.XPATH, '//*[@id="input19-282"]', config.SAPELLIDO) # Ingreso de datos en el formulario del Segundo Apellido
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input23-289"]')))  # Ingreso de correo electrónico
        email_field.send_keys(config.EMAIL)
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-292"]', config.CIUDAD) # Datos de la ciudad
        dropdown_option = WebDriverWait(driver, 10).until(  # Selección de la ciudad (con una espera explícita)
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='BOGOTA']")
            )
        )
        ActionChains(driver).move_to_element(dropdown_option).perform()  # Desplazarse al elemento
        dropdown_option.click()  # Selección de la opción       
        hidden_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input25-296"]')))  # validar que el departamento sea el correcto
        hidden_value = hidden_field.get_attribute(config.DEPARTAMENTO)  # Obtener valor de un campo oculto
        country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input27-298"]'))) # validar que el pais sea el correcto
        country_value = country_field.get_attribute(config.PAIS)  # Obtener valor de país
        input_field = WebDriverWait(driver, 10).until(  # Espera explícita hasta que el campo de teléfono esté presente en el DOM.
            EC.presence_of_element_located((By.XPATH, '//*[@id="input33-304"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_field)  # Desplaza el campo de teléfono a la vista.
        driver.execute_script("arguments[0].click();", input_field)  # Hace clic en el campo de teléfono para activarlo.
        ActionChains(driver).move_to_element(input_field).click().send_keys(config.TELEFONO).perform()  # Mueve al campo de teléfono, hace clic y envía el número de teléfono.
        self.enter_text(driver, By.XPATH, '//*[@id="inputId-307"]', config.EVENTO) # Datos del evento
        dropdown_option = WebDriverWait(driver, 10).until(  # Selección del evento (esperar la opción visible y hacer clic)
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='FERIA DEL LIBRO 2024']")
            )
        )
        ActionChains(driver).move_to_element(dropdown_option).perform()  # Desplaza el cursor hasta la opción del dropdown.
        dropdown_option.click()  # Hace clic en la opción del dropdown.
        checkbox = WebDriverWait(driver, 20).until( # Marcar checkbox
            EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-checkbox_faux"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)  # Desplaza el checkbox a la vista.
        ActionChains(driver).move_to_element(checkbox).click().perform()  # Mueve al checkbox y lo selecciona.
        batons = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc/slot/c-global-onboarding-custom-button-cmp/div/button'))
        )  # Espera hasta que el botón "Siguiente" esté clickeable.
        batons.click()  # Hace clic en el botón "Siguiente".
        time.sleep(15)  # Espera 15 segundos para garantizar que la acción se complete.
        print("Validación Datos de contacto")

    def personal_form(self, driver):
        self.enter_text(driver, By.XPATH, "//input[@data-id='date-picker-slds-input']", '12/28/1984') # Ingresar la fecha en el campo de fecha usando el input de tipo date
        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-351"]')  # Encuentra el combobox (desplegable) para seleccionar un valor.
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el combobox a la vista.
        dropdown.click()  # Hace clic en el combobox para mostrar las opciones.
        wait = WebDriverWait(driver, 10)  # Configura la espera explícita para el siguiente paso.
        option_xpath = f'//div[@role="option" and @data-value="Masculino"]'  # XPath para la opción "Masculino" en el dropdown.
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))  # Espera hasta que la opción esté clickeable.
        time.sleep(2)  # Pausa de 2 segundos para garantizar la interacción completa.
        option.click()  # Hace clic en la opción "Masculino".
        radio = self.wait_for_element(driver, By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")  # Espera hasta que el radio button sea visible.
        driver.execute_script("arguments[0].click();", radio)  # Usa Javascript para hacer clic en el radio button.
        dropdown = driver.find_element(By.XPATH, '//*[@id="comboboxId-376"]')  # Encuentra el dropdown.
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el dropdown a la vista si es necesario.
        dropdown.click()  # Hace clic para desplegar las opciones del dropdown.
        wait = WebDriverWait(driver, 10)  # Configura la espera explícita para el siguiente paso.
        one_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="01"]]')))  # Espera hasta que la opción "01" sea clickeable.
        one_option.click()  # Hace clic en la opción "01".
        time.sleep(2)  # Pausa de 2 segundos para garantizar que la acción se complete.
        self.enter_text(driver, By.XPATH, '//*[@id="input41-384"]', config.NOMBRED)  # Ingresa el nombre en el campo correspondiente.
        self.enter_text(driver, By.XPATH, '//*[@id="input43-386"]', config.PAPELLIDOD)  # Ingresa el primer apellido en el campo correspondiente.
        self.enter_text(driver, By.XPATH, '//*[@id="input45-388"]', config.SAPELLIDOD)  # Ingresa el segundo apellido en el campo correspondiente.
        self.select_dropdown_option(driver, '//*[@id="comboboxId-390"]', '//div[@role="option" and .//span[text()="Hijo/a"]]')  # Selecciona la opción "Hijo/a" en el dropdown.
        date_input = driver.find_element(By.XPATH, '//*[@id="date-input-394"]')  # Encuentra el campo de fecha.
        date_input.send_keys('01/18/1970')  # Ingresa la fecha manualmente (por ejemplo, 01/18/1970).
        time.sleep(8)  # Espera 8 segundos para asegurar que la fecha se haya ingresado correctamente.
        date_input.click()  # Hace clic en el campo para completar la interacción.
        save_button = self.wait_for_element(driver, By.XPATH, '//button[contains(text(), "Guardar y continuar")]')  # Espera hasta que el botón esté visible.
        self.scroll_into_view(driver, save_button)  # Desplaza el botón a la vista si no está visible.
        save_button.click()  # Hace clic en el botón para continuar.
        time.sleep(5)  # Espera 5 segundos para asegurar que la acción se haya completado.
        print("Validación Información Personal")
        pass

    def perfil_financiero(self, driver):
        wait = WebDriverWait(driver, 30)  # Espera explícita de 30 segundos para que los elementos estén disponibles.
        elements = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")  
        print(f"Elementos encontrados: {len(elements)}")  # Imprime la cantidad de elementos encontrados.
        promedio = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))  
        # Espera hasta que el campo de texto sea clickeable.
        promedio.click()  # Hace clic en el campo de texto.
        promedio.send_keys("0 a 4.000.000")  # Ingresa el texto "0 a 4.000.000" en el campo de texto.
        # Selección de la opción en el desplegable (espera explícita)
        promedio_option = wait.until(EC.visibility_of_element_located(
        (
            By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='0 a 4.000.000']")
        ))  # Espera hasta que la opción "0 a 4.000.000" sea visible.
        ActionChains(driver).move_to_element(promedio_option).perform()  # Desplaza el mouse sobre la opción.
        promedio_option.click()  # Hace clic en la opción seleccionada.
        time.sleep(2) # Espera de 2 segundos antes de continuar con la siguiente acción para permitir que el navegador procese la información
        empleado_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[2]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"))
        )  # Espera hasta que el campo de selección de "Empleado" sea clickeable.
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", empleado_option)  # Hacer scroll hasta el checkbox para asegurarse de que está visible en la pantalla
        empleado_option.click()  # Hace clic en el campo de selección.
        time.sleep(2)
        empleado_option.send_keys("Empleado")  # Ingresa "Empleado" en el campo.
        empleado_option_text = WebDriverWait(driver, 10).until( # Espera explícita hasta que la opción 'Empleado' sea visible en la lista
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='Empleado']")
            )
        )
        ActionChains(driver).move_to_element(empleado_option_text).perform() # Desplazarse al elemento 'Empleado' para asegurarse de que esté visible antes de hacer clic
        empleado_option_text.click() # Hacer clic en la opción 'Empleado'
        currency_input = WebDriverWait(driver, 10).until(   # Espera explícita hasta que el campo de entrada de moneda sea clickeable
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-currency[1]/slot[1]/c-masked-input[1]/div[1]/div[2]/input[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", currency_input)  # Hacer scroll hasta el checkbox para asegurarse de que está visible en la pantalla
        currency_input.click() # Hacer clic en el campo de entrada de moneda para activarlo
        currency_input.send_keys("1000000") # Ingresar el valor de 1.000.000 en el campo
        time.sleep(2) # Esperar 2 segundos para asegurar que el valor se haya ingresado correctamente
        checkbox_xpaths = [  # Lista de XPaths para los checkboxes, que están ubicados en diferentes partes de la página web
            # XPath para el primer checkbox: Localizado en un grupo de selección múltiple
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/span[1]",
            # XPath para el segundo checkbox: Ubicado en otro punto dentro del mismo grupo de selección múltiple
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[4]/label[1]/span[1]",
            # XPath para el tercer checkbox: Ubicado en otra parte del grupo de selección múltiple
            "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[1]/slot[1]/c-checkbox-group[1]/div[1]/fieldset[1]/div[1]/div[6]/label[1]/span[1]"
        ]
        for xpath in checkbox_xpaths:  # Recorrer la lista de XPaths y seleccionar cada checkbox con scroll automático
            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))) # Esperar hasta que el elemento (checkbox) esté presente en la página
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)  # Hacer scroll hasta el checkbox para asegurarse de que está visible en la pantalla
            ActionChains(driver).move_to_element(checkbox).perform() # Alternativa: Usar la acción de mover el mouse hasta el elemento con las teclas de flecha para garantizar que esté en la vista
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click() # Esperar a que el checkbox sea clickeable y hacer clic en él
            # Definir la ruta XPath de la imagen que se quiere interactuar
            image_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[2]/slot[1]/c-checkbox-image-group[1]/div[1]/div[1]/fieldset[1]/div[1]/div[2]/label[1]/div[1]"
            image_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))  # Esperar hasta que la imagen esté presente en el DOM
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", image_element) # Desplazar la página hasta la imagen para asegurarse de que sea visible
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, image_xpath))).click() # Esperar a que la imagen sea clickeable y hacer clic
        # XPath del botón a hacer clic
        button_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-custom-lwc[1]/slot[1]/c-global-onboarding-custom-button-cmp[1]/div[1]/button[2]"
        button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath))) # Esperar a que el botón esté presente en el DOM
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_element) # Hacer scroll hasta el botón para asegurarnos de que sea visible
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click() # Esperar a que el botón sea clickeable y hacer clic
        time.sleep(30) # Espera 30 segundos para asegurar que la acción se haya completado.
        print("Validación Perfil Financiero")
        pass

    def metas_fiancieras(self, driver):
        # XPath del botón o elemento al que quieres hacer scroll
        element_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-navigate-action[1]/slot/c-navigate-action/slot/div/c-button/button"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))  # Esperar a que el elemento esté presente en el DOM        
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element) # Hacer scroll hasta el elemento utilizando JavaScript
        # XPath del elemento que contiene el texto a verificar
        text_xpath = "//*[@id='brandBand_2']/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-custom-lwc[2]/slot/c-global-onboarding-comparador-cmp/main/section[1]/c-global-onboarding-product-card-cmp/article/header/div/h2"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text_xpath))) # Esperar a que el elemento esté presente
        element_text = element.text # Obtener el texto del elemento
        element_text == "Solución educativa"
        # XPath del botón al que se debe hacer clic
        button_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-custom-lwc[2]/slot/c-global-onboarding-comparador-cmp/main/section[1]/c-global-onboarding-product-card-cmp/article/section/div[1]/button"
        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))) # Esperar a que el botón esté presente
        button_element.click() # Hacer clic en el botón
        time.sleep(30) # Espera 30 segundos para asegurar que la acción se haya completado.
        print("Validación Metas Financieras")
        pass

def test_consulta(driver: WebDriver):
        test = TestConsulta() # Crear una instancia de la clase TestConsulta, que contiene los métodos necesarios para interactuar con la página web.
        test.login(driver, config.USERNAME, config.PASSWORD) # Llamada al método login para iniciar sesión en la aplicación con el nombre de usuario y contraseña proporcionados en el archivo de configuración.
        test.complete_form(driver) # Llamada al método complete_form para completar el formulario principal de la aplicación utilizando el driver de Selenium.
        test.validate_second_form(driver) # Llamada al método validate_second_form para verificar que el segundo formulario o paso de la aplicación se haya cargado correctamente.
        test.personal_form(driver) # Llamada al método personal_form para completar el formulario con la información personal del usuario.
        test.perfil_financiero(driver) # Llamada al método perfil_financiero para completar o validar el perfil financiero del usuario en la aplicación.
        test.metas_fiancieras(driver) # Llamada al método metas_finaciera para completar o validar el metas finaciera.