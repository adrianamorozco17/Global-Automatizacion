from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from config import config
from utils.helpers import generar_identificacion_aleatoria
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas


class ConsultaPage(BasePage):
    def login(self):
        self.open_url("https://globalseguros--qaonb.sandbox.my.salesforce.com/")
        self.enter_text(By.CSS_SELECTOR, "input[name='username']", config.USERNAME)
        self.enter_text(By.ID, 'password', config.PASSWORD)
        self.click_element(By.CSS_SELECTOR, "input[id='Login']")
        time.sleep(15)
        print("Ingreso Login")

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