from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from utils.helpers import generar_identificacion_aleatoria
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas


class FormPage(BasePage):
    def complete_form(self):
        """ Completa el formulario inicial """
        target_url = "https://globalseguros--qaonb.sandbox.lightning.force.com/lightning/cmp/vlocity_ins__vlocityLWCOmniWrapper?c__target=c%3AgsvFormularyEnglish&c__layout=lightning&c__tabLabel=Perfilamiento"
        self.open_url(target_url)

        # Seleccionar opción en el dropdown
        self.select_dropdown_option(
            (By.XPATH, '//*[@id="comboboxId-211"]'),
            (By.XPATH, '//div[@role="option" and .//span[text()="CEDULA DE CIUDADANIA"]]')
        )

        # Generar e ingresar número de identificación aleatorio
        numero_identificacion = generar_identificacion_aleatoria()
        self.enter_text(By.XPATH, '//*[@id="input1-214"]', numero_identificacion)

        # Ingresar nombre del asesor
        self.enter_text(By.XPATH, '//*[@id="inputId-227"]', config.ASESOR)

        # Esperar y seleccionar una opción en el dropdown
        dropdown_option = self.wait_for_element(By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and contains(text(), 'PROYECTA-T LTDA-BOGOTA')]")

        # Mueve el cursor hasta la opción y selecciona
        ActionChains(self.driver).move_to_element(dropdown_option).perform()
        dropdown_option.click()

        # Hacer clic en "Siguiente"
        next_button = self.wait_for_element(By.XPATH, "//button[.//span[text()='Siguiente']]")
        self.scroll_into_view(next_button)
        next_button.click()

        print("Formulario inicial completado")

    def validate_second_form(self):
        # Valida y completa el segundo formulario en el proceso de automatización.
        # Args: driver (webdriver): Instancia del navegador en uso.
        wait = WebDriverWait(self.driver, 10)  # Espera explícita hasta que el formulario esté listo para ser validado.
        self.enter_text(By.XPATH, '//*[@id="input15-278"]', config.NOMBRE) # Ingreso de datos en el formulario de los Nombres
        self.enter_text(By.XPATH, '//*[@id="input17-280"]', config.PAPELLIDO) # Ingreso de datos en el formulario del Primer Apellido
        self.enter_text(By.XPATH, '//*[@id="input19-282"]', config.SAPELLIDO) # Ingreso de datos en el formulario del Segundo Apellido
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input23-289"]')))  # Ingreso de correo electrónico
        email_field.send_keys(config.EMAIL)
        self.enter_text(By.XPATH, '//*[@id="inputId-292"]', config.CIUDAD) # Datos de la ciudad
        dropdown_option = WebDriverWait(self.driver, 10).until(  # Selección de la ciudad (con una espera explícita)
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='BOGOTA']")
            )
        )
        ActionChains(self.driver).move_to_element(dropdown_option).perform()  # Desplazarse al elemento
        dropdown_option.click()  # Selección de la opción       
        hidden_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input25-296"]')))  # validar que el departamento sea el correcto
        hidden_value = hidden_field.get_attribute(config.DEPARTAMENTO)  # Obtener valor de un campo oculto
        country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input27-298"]'))) # validar que el pais sea el correcto
        country_value = country_field.get_attribute(config.PAIS)  # Obtener valor de país
        input_field = WebDriverWait(self.driver, 10).until(  # Espera explícita hasta que el campo de teléfono esté presente en el DOM.
            EC.presence_of_element_located((By.XPATH, '//*[@id="input33-304"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_field)  # Desplaza el campo de teléfono a la vista.
        self.driver.execute_script("arguments[0].click();", input_field)  # Hace clic en el campo de teléfono para activarlo.
        ActionChains(self.driver).move_to_element(input_field).click().send_keys(config.TELEFONO).perform()  # Mueve al campo de teléfono, hace clic y envía el número de teléfono.
        self.enter_text(By.XPATH, '//*[@id="inputId-307"]', config.EVENTO) # Datos del evento
        dropdown_option = WebDriverWait(self.driver, 10).until(  # Selección del evento (esperar la opción visible y hacer clic)
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='FERIA DEL LIBRO 2024']")
            )
        )
        ActionChains(self.driver).move_to_element(dropdown_option).perform()  # Desplaza el cursor hasta la opción del dropdown.
        dropdown_option.click()  # Hace clic en la opción del dropdown.
        checkbox = WebDriverWait(self.driver, 20).until( # Marcar checkbox
            EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-checkbox_faux"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", checkbox)  # Desplaza el checkbox a la vista.
        ActionChains(self.driver).move_to_element(checkbox).click().perform()  # Mueve al checkbox y lo selecciona.
        batons = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc/slot/c-global-onboarding-custom-button-cmp/div/button'))
        )  # Espera hasta que el botón "Siguiente" esté clickeable.
        batons.click()  # Hace clic en el botón "Siguiente".
        time.sleep(15)  # Espera 15 segundos para garantizar que la acción se complete.
        print("Validación Datos de contacto")