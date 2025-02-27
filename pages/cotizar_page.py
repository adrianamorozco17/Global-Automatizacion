from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from utils.helpers import generar_nombre_completo
from utils.helpers import generar_identificacion_aleatoria
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas

class CotizarFormPage(BasePage):
    def datos_asegurado(self):
        boton_continuar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Guardar y continuar']]"))
        )
        # Hacer scroll hasta el botón
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_continuar)
        # Mover el cursor al botón y hacer clic
        ActionChains(self.driver).move_to_element(boton_continuar).click().perform()
        pass

    def datos_beneficiario(self):
        # Generar datos aleatorios
        nombre, apellido1, apellido2 = generar_nombre_completo()
        numero= generar_identificacion_aleatoria()
        print(f"Ingresando: {nombre} {apellido1} {apellido2}")

        # Esperar 2 segundos antes de buscar los elementos
        time.sleep(2)

        # Buscar los campos por su placeholder
        campo_nombre = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Nombres completos']"))
        )
        time.sleep(1)  # Espera antes de escribir
        campo_nombre.click()
        campo_nombre.send_keys(nombre)
        time.sleep(1)
     
        # Esperar hasta que el campo sea interactivo
        campo_apellido1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Primer Apellido']"))
        )
        
        time.sleep(1)  # Pausa opcional para evitar problemas

        campo_apellido1.send_keys(apellido1)  # Ingresar apellido
        time.sleep(1)

        campo_apellido2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Segundo Apellido']"))
        )
        
        time.sleep(1)  # Pausa opcional para evitar problemas

        campo_apellido2.send_keys(apellido2)  #
        time.sleep(1)
        combobox_tipo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'slds-combobox__form-element')]//input"))
        )

        combobox_tipo.click()

        #Esperar a que se despliegue la lista de opciones
        option_xpath = "//*[contains(@class, 'slds-listbox')]/descendant::*[contains(text(), 'Tarjeta de Identidad')]"

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )

        #Hacer clic en la opción correcta
        option.click()
        time.sleep(2)
        campo_numero = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresar número']"))
        )
        time.sleep(1)  # Pequeña pausa
        campo_numero.send_keys(str(numero))  # Ingresar número
        time.sleep(1)  # Pequeña pausa
        campo_fecha = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Fecha de Nacimiento']"))
        )
        time.sleep(1)  # Pequeña pausa
        campo_fecha.send_keys('18-02-2020')  # Ingresa la fecha manualmente (por ejemplo, 01/18/1970).
        time.sleep(5)  # Pequeña pausa
        wait = WebDriverWait(self.driver, 20)
        # Esperar a que el combobox sea visible y clickable
        combobox_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[2]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))
        combobox_input.click()  # Asegurar que el dropdown se despliegue
        combobox_input.send_keys("Femenino")
        wait = WebDriverWait(self.driver, 20)  # Aumentado a 20 segundos
        opcion_femenino = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[2]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[2]/div/ul/li[3]/div")))
        opcion_femenino.click()
        time.sleep(10)  # Pequeña pausa
            
    def boton_guardar(self):
        wait = WebDriverWait(self.driver, 20)
        boton_guardar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Guardar y continuar']]")))

        # Hacer scroll hasta el botón
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", boton_guardar)

        # Pequeña pausa para que la animación termine
        time.sleep(1)

        # Usar ActionChains para hacer clic
        ActionChains(self.driver).move_to_element(boton_guardar).click().perform()

        # Otra pausa corta si es necesario antes de continuar con otros pasos
        time.sleep(2)
        print("Validación Información beneficiario")
        pass

    def button_regresar(self):
        boton_anterior = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='button-container']/button[1]"))
        )
        boton_anterior.click()  
        pass
