from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from utils.helpers import generar_identificacion_aleatoria
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas

class MetasFormPage(BasePage):
    def metas_fiancieras(self):
        # XPath del botón o elemento al que quieres hacer scroll
        element_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-navigate-action[1]/slot/c-navigate-action/slot/div/c-button/button"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))  # Esperar a que el elemento esté presente en el DOM        
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element) # Hacer scroll hasta el elemento utilizando JavaScript
        # XPath del elemento que contiene el texto a verificar
        time.sleep(3)
        text_xpath = "//*[@id='brandBand_2']/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-custom-lwc[2]/slot/c-global-onboarding-comparador-cmp/main/section[1]/c-global-onboarding-product-card-cmp/article/header/div/h2"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, text_xpath))) # Esperar a que el elemento esté presente
        element_text = element.text # Obtener el texto del elemento
        element_text == "Solución educativa"
        time.sleep(5)
        # XPath del botón al que se debe hacer clic
        pass


    def button_cotizar(self):
        button_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-data-comparador-english/div/article/div[2]/vlocity_ins-omniscript-step/div[3]/slot/vlocity_ins-omniscript-custom-lwc[2]/slot/c-global-onboarding-comparador-cmp/main/section[1]/c-global-onboarding-product-card-cmp/article/section/div[1]/button"
        button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))) # Esperar a que el botón esté presente
        button_element.click() # Hacer clic en el botón
        time.sleep(30) # Espera 30 segundos para asegurar que la acción se haya completado.
        print("Validación Metas Financieras")
        pass


    def button_regreso(self):
        boton_regresar_p = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[./span[text()='Regresar al perfilamiento']]"))
        )
        boton_regresar_p.click()      
        pass
    

    def button_comprador(self):
        boton_comprador = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[./span[text()='Regresar al comparador']]"))
    )
        boton_comprador.click()
    pass
