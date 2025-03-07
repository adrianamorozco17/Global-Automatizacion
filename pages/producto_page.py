from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas
from selenium.webdriver.common.keys import Keys



class ProductoFormPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Inicializar `wait` correctamente

    def datos_producto(self):
        # Esperar a que el combobox sea visible y clickeable
        combobox_año = self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc[1]/slot/c-gsv-year-select-cmp/lightning-combobox/div/div[1]/lightning-base-combobox/div/div/div[1]/button"))
        )
        combobox_año.click()  # Desplegar el dropdown

        # Esperar la opción del año 2038 y seleccionarla
        opcion_2038 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//lightning-base-combobox-item[@data-value='2038']")))
        opcion_2038.click()
        time.sleep(2)
        observaciones = self.wait.until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-text/slot/c-input/div/div[2]/input")))
        observaciones.click()
        observaciones.send_keys("Ninguno")
        print("Año de ingreso a cotizar")
    pass

    def datos_producto_segura_plus(self):
        # Espera hasta que el campo sea clickeable y luego hace clic en él
        wait = WebDriverWait(self.driver, 30)  # Espera hasta 30 segundos
        producto = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))

        # Asegura que el campo esté visible
        self.driver.execute_script("arguments[0].scrollIntoView();", producto)
        producto.click()  # Hace clic en el campo

        # Ingresa el texto y confirma con ENTER
        producto.send_keys(config.PRODUCTO1)
        producto.send_keys(Keys.RETURN)  # Simula presionar Enter

        # Espera hasta que la opción sea seleccionable y haz clic
        prod_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[2]/div/ul/li[2]/div/span/span")))
        ActionChains(self.driver).move_to_element(prod_option).click().perform()

        time.sleep(5)
        #MES
        wait = WebDriverWait(self.driver, 30)  # Espera hasta 10 segundos
        tarifa = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[8]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))
        self.driver.execute_script("arguments[0].scrollIntoView();", tarifa)
        self.driver.execute_script("arguments[0].click();", tarifa)
        tarifa.clear()
        tarifa.send_keys(config.MES_TARIFA)
        tarifa.send_keys(Keys.RETURN)  # Simula presionar Enter
        tarifa_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[8]/slot/c-combobox/div/div/div[2]/div[2]/div/ul/li[2]/div/span/span")))
        ActionChains(self.driver).move_to_element(tarifa_option).click().perform()
        time.sleep(5)
        #asegurado
        valor_asegu = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[15]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))  
        self.driver.execute_script("arguments[0].scrollIntoView();", valor_asegu)
        valor_asegu.click()  
        valor_asegu.send_keys(config.VALOR_ASEGURADO)  # Ingresa el texto "1.000.000" en el campo de texto.
        # Selección de la opción en el desplegable (espera explícita)
        valor_asegu_option = wait.until(EC.visibility_of_element_located(
        (
            By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='1.000.000']")
        ))  # Espera hasta que la opción "0 a 4.000.000" sea visible.
        ActionChains(self.driver).move_to_element(valor_asegu_option).perform()  # Desplaza el mouse sobre la opción.
        valor_asegu_option.click()  # Hace clic en la opción seleccionada.
        time.sleep(5)
    pass


    def button_cotizar(self):
        button_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/div[2]/div[1]/div/vlocity_ins-button[1]/button"
        button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath))) # Esperar a que el botón esté presente en el DOM
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_element) # Hacer scroll hasta el botón para asegurarnos de que sea visible
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click() # Esperar a que el botón sea clickeable y hacer clic
        time.sleep(30) # Espera 30 segundos para asegurar que la acción se haya completado.
        print("Validación Perfil Financiero")
        pass