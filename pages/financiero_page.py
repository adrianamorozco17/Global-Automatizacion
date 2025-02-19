from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas


class FinancieroFormPage(BasePage):
    def perfil_financiero(self):
        wait = WebDriverWait(self.driver, 30)  # Espera explícita de 30 segundos para que los elementos estén disponibles.
        elements = self.driver.find_elements(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")  
        print("Elementos encontrados: {len(elements)}")  # Imprime la cantidad de elementos encontrados.
        promedio = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[1]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))  
        # Espera hasta que el campo de texto sea clickeable.
        promedio.click()  # Hace clic en el campo de texto.
        promedio.send_keys(config.PROMEDIO)  # Ingresa el texto "0 a 4.000.000" en el campo de texto.
        # Selección de la opción en el desplegable (espera explícita)
        promedio_option = wait.until(EC.visibility_of_element_located(
        (
            By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='0 a 4.000.000']")
        ))  # Espera hasta que la opción "0 a 4.000.000" sea visible.
        ActionChains(self.driver).move_to_element(promedio_option).perform()  # Desplaza el mouse sobre la opción.
        promedio_option.click()  # Hace clic en la opción seleccionada.
        # Esperar a que el campo sea clickeable
        empleado_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
            "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[1]/div/input"))
        )
        # Hacer scroll hasta el elemento
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",empleado_option)
        time.sleep(1)  # Pausa para evitar que otro elemento bloquee el clic
        actions = ActionChains(self.driver)
        actions.move_to_element(empleado_option).click().perform()
        time.sleep(1)  # Pausa para evitar que otro elemento bloquee el clic
        # Hacer clic en el campo para abrir la lista
        empleado_option.send_keys("Empleado")  # Ingresa "Empleado" en el campo.
        empleado_option_text = WebDriverWait(self.driver, 10).until(
            # Espera explícita hasta que la opción 'Empleado' sea visible en la lista
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='Empleado']")
            )
        )
        empleado_option_text.click() # Hacer clic en la opción 'Empleado'
        time.sleep(1)  # Pausa para evitar que otro elemento bloquee el clic
        ahorros_input = WebDriverWait(self.driver, 10).until(   # Espera explícita hasta que el campo de entrada de moneda sea clickeable
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-currency[1]/slot[1]/c-masked-input[1]/div[1]/div[2]/input[1]"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ahorros_input)  # Hacer scroll hasta el checkbox para asegurarse de que está visible en la pantalla
        ahorros_input.click() # Hacer clic en el campo de entrada de moneda para activarlo
        ahorros_input.send_keys(config.VALOR_APROX) # Ingresar el valor de 1.000.000 en el campo
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
            checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))) # Esperar hasta que el elemento (checkbox) esté presente en la página
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)  # Hacer scroll hasta el checkbox para asegurarse de que está visible en la pantalla
            ActionChains(self.driver).move_to_element(checkbox).perform() # Alternativa: Usar la acción de mover el mouse hasta el elemento con las teclas de flecha para garantizar que esté en la vista
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click() # Esperar a que el checkbox sea clickeable y hacer clic en él
            # Definir la ruta XPath de la imagen que se quiere interactuar
            image_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-multiselect[2]/slot[1]/c-checkbox-image-group[1]/div[1]/div[1]/fieldset[1]/div[1]/div[2]/label[1]/div[1]"
            image_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))  # Esperar hasta que la imagen esté presente en el DOM
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", image_element) # Desplazar la página hasta la imagen para asegurarse de que sea visible
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, image_xpath))).click() # Esperar a que la imagen sea clickeable y hacer clic
        # XPath del botón a hacer clic
    
    def button_siguiente(self):
        button_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-formulary-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[6]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-custom-lwc[1]/slot[1]/c-global-onboarding-custom-button-cmp[1]/div[1]/button[2]"
        button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath))) # Esperar a que el botón esté presente en el DOM
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_element) # Hacer scroll hasta el botón para asegurarnos de que sea visible
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click() # Esperar a que el botón sea clickeable y hacer clic
        time.sleep(30) # Espera 30 segundos para asegurar que la acción se haya completado.
        print("Validación Perfil Financiero")
        pass

    def button_anterior(self):
        boton_regresar= WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Anterior']"))
        )
        boton_regresar.click()       
        pass