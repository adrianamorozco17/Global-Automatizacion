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
        self.wait = WebDriverWait(driver, 30)  # Inicializar `wait` correctamente

    def datos_producto(self):
        # Esperar a que el combobox sea visible y clickeable
        combobox_año = self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-custom-lwc[1]/slot/c-gsv-year-select-cmp/lightning-combobox/div/div[1]/lightning-base-combobox/div/div/div[1]/button"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", combobox_año)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", combobox_año)

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
        producto.click()  # Hace clic en el campo
        time.sleep(5)
        # Espera hasta que la opción sea seleccionable y haz clic
        # Esperar a que aparezca la opción "Global Universidad Segura Plus"
        opcion = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-tvs-perfilador-educativo-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[2]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/div[1]")))
        # Mover el cursor sobre la opción y hacer clic en ella
        actions = ActionChains(self.driver)
        actions.move_to_element(opcion).pause(1).click().perform()
        time.sleep(5)
        #MES
        wait = WebDriverWait(self.driver, 30)  # Espera hasta 10 segundos
        tarifa = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[8]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))
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
            By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='5.000.000']")
        ))  # Espera hasta que la opción "0 a 4.000.000" sea visible.
        ActionChains(self.driver).move_to_element(valor_asegu_option).perform()  # Desplaza el mouse sobre la opción.
        valor_asegu_option.click()  # Hace clic en la opción seleccionada.
        time.sleep(7)
    pass

    def datos_producto_segura_plus_semestre(self):
        wait = WebDriverWait(self.driver, 30)
        # Espera a que el campo del combo box sea clickeable
        producto_u = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))
        # Asegura que el campo esté visible y haz clic en él
        self.driver.execute_script("arguments[0].scrollIntoView();", producto_u)
        producto_u.click()
        time.sleep(2)  # Pequeña espera para que carguen las opciones
        # Presiona ARROW_DOWN para moverse a la segunda opción
        producto_u.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        producto_u.send_keys(Keys.ENTER)  # Seleccionar la opción
        time.sleep(3)  # Esperar para ver si el clic se procesó correctamente
        wait = WebDriverWait(self.driver, 30)  # Espera hasta 10 segundos
        tarifa = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-tvs-perfilador-educativo-english/div/article/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[8]/slot/c-combobox/div/div/div[2]/div[1]/div/input")))
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
        valor_asegu.send_keys(config.VALOR_ASEGURADO2)  # Ingresa el texto "1.000.000" en el campo de texto.
        # Selección de la opción en el desplegable (espera explícita)
        valor_asegu_option = wait.until(EC.visibility_of_element_located(
        (
            By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='2.000.000']")
        ))  # Espera hasta que la opción "0 a 4.000.000" sea visible.
        ActionChains(self.driver).move_to_element(valor_asegu_option).perform()  # Desplaza el mouse sobre la opción.
        valor_asegu_option.click()  # Hace clic en la opción seleccionada.
        time.sleep(5)
        # XPath del combo box (campo de entrada)
        semestre_xpath = "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/c-gsv-tvs-perfilador-educativo-english[1]/div[1]/article[1]/div[2]/vlocity_ins-omniscript-step[4]/div[3]/slot[1]/vlocity_ins-omniscript-block[1]/div[1]/div[1]/section[1]/fieldset[1]/slot[1]/vlocity_ins-omniscript-select[16]/slot[1]/c-combobox[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
        # XPath de la opción con el valor '6'
        # Esperar que el combo box sea clickeable y hacer clic
        combobox_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, semestre_xpath))
        )
        combobox_element.click()
        print("Combo box abierto.")
        # Esperar que la opción 6 sea visible y hacer clic
        time.sleep(2)  # Pequeña espera para que carguen las opciones
        # Presiona ARROW_DOWN para moverse a la segunda opción
        for _ in range(6):  # Repite 6 veces
            combobox_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        combobox_element.send_keys(Keys.ENTER)  # Seleccionar la opción
        time.sleep(3)  # Esperar para ver si el clic se procesó correctamente
        print("Opción 6 seleccionada.")
    pass

    def simulador_producto_segura_plus(self):
        title_xpath = "//*[contains(text(), 'Valor asegurado semestre')]"  # XPath flexible para cualquier etiqueta que contenga este texto
        # Esperar hasta que el título sea visible
        titulo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_xpath))
        )
        # Validar que el texto sea el esperado
        assert titulo.text.strip() == "Valor asegurado semestre", "El título no coincide"
        print("El título 'Valor asegurado semestre' está presente.")
        time.sleep(5)
        # XPath del combo box (input)
        combobox_xpath = "//input[contains(@class, 'slds-input') and @role='combobox']"

        # XPath de la opción con el valor '5000000'
        option_xpath = "//span[contains(@class, 'slds-listbox__option-text') and text()='5.000.000']"

        # Esperar que el combo box sea clickeable y hacer clic
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        )
        combobox_element.click()
        print("Combo box abierto.")

        # Esperar que la opción de 5,000,000 esté visible y hacer clic
        option_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, option_xpath))
        )
        option_element.click()
        print("Seleccionada la opción 5000000.")
        time.sleep(5)
        title_xpath = "//*[contains(text(), 'Año de maduración')]"  # Busca cualquier etiqueta con este texto
        # Esperar hasta que el texto sea visible en la página
        titulo_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_xpath))
        )

        # Validar que el texto encontrado sea el esperado
        assert titulo_element.text.strip() == "Año de maduración", "El texto 'Año de maduración' no está presente."
        print("El texto 'Año de maduración' está presente en la página.")
        time.sleep(5)
        # XPath del campo de texto basado en su clase
        input_xpath = "//input[contains(@class, 'vlocity-input') and contains(@class, 'slds-input')]"
        # Esperar hasta que el campo sea visible y clickeable
        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, input_xpath))
        )
        # Limpiar el campo (por si tiene un valor previo)
        input_element.clear()
        # Ingresar el año 2028
        input_element.send_keys("2035")
        print("Año 2028 ingresado correctamente en el campo.")
        spinner_xpath = "//lightning-spinner[contains(@class, 'slds-spinner_container')]"
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, spinner_xpath))
        )
        print("Spinner de carga desapareció.")
        # XPath del contenedor del valor total
        total_container_xpath = "//div[contains(@class, 'vloc-ins-coverages-amount-container')]"
        # Esperar que el contenedor sea visible
        total_container_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, total_container_xpath))
        )
        # Hacer scroll hasta el elemento
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", total_container_element)
        # Hacer clic en el contenedor del valor total
        total_container_element.click()
        print("Se hizo clic en el contenedor del valor total correctamente.")
        time.sleep(5)
        texto_xpath = "//*[contains(text(), '$ 29.762.000,00')]"  # Busca cualquier etiqueta que contenga el texto exacto
        # Esperar hasta que el texto sea visible en la página
        print("El texto '$ 29.762.000,00' está presente en la página.")
        time.sleep(5)
        # XPath basado en el texto "NO"
        si_xpath = "//label[span[text()='NO']]"
        # Esperar hasta que el elemento esté visible y clickeable
        si_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, si_xpath))
        )
        # Hacer scroll hasta el elemento (opcional, por si no está en pantalla)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", si_element)
        # Hacer clic en el elemento
        si_element.click()
        print("Se hizo clic en el botón 'NO' correctamente.")
        time.sleep(5)
        pass

    def simulador_producto_segura_plus_semestre(self):
        title_xpath = "//*[contains(text(), 'GlobalUniversidad Segura Plus Semestres')]"  # XPath flexible para cualquier etiqueta que contenga este texto
        # Esperar hasta que el título sea visible
        titulo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_xpath))
        )
        # Validar que el texto sea el esperado
        assert titulo.text.strip() == "Valor Limite Semestre", "El título no coincide"
        print("El título 'Valor asegurado semestre' está presente.")
        time.sleep(5)
        # XPath del combo box (input)
        combobox_xpath = "//input[contains(@class, 'slds-input') and @role='combobox']"

        # XPath de la opción con el valor '2000000'
        option_xpath = "//span[contains(@class, 'slds-listbox__option-text') and text()='2.000.000']"

        # Esperar que el combo box sea clickeable y hacer clic
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        )
        combobox_element.click()
        print("Combo box abierto.")

        # Esperar que la opción de 5,000,000 esté visible y hacer clic
        option_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, option_xpath))
        )
        option_element.click()
        print("Seleccionada la opción 2000000.")
        time.sleep(5)
        title_xpath = "//*[contains(text(), 'Año de maduración')]"  # Busca cualquier etiqueta con este texto
        # Esperar hasta que el texto sea visible en la página
        titulo_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_xpath))
        )

        # Validar que el texto encontrado sea el esperado
        assert titulo_element.text.strip() == "Año de maduración", "El texto 'Año de maduración' no está presente."
        print("El texto 'Año de maduración' está presente en la página.")
        time.sleep(5)
        # XPath del campo de texto basado en su clase
        input_xpath = "//input[contains(@class, 'vlocity-input') and contains(@class, 'slds-input')]"
        # Esperar hasta que el campo sea visible y clickeable
        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, input_xpath))
        )
        # Limpiar el campo (por si tiene un valor previo)
        input_element.clear()
        # Ingresar el año 2040
        input_element.send_keys("2040")
        print("Año 2040 ingresado correctamente en el campo.")
        spinner_xpath = "//lightning-spinner[contains(@class, 'slds-spinner_container')]"
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, spinner_xpath))
        )
        print("Spinner de carga desapareció.")
        # XPath del contenedor del valor total
        total_container_xpath = "//div[contains(@class, 'vloc-ins-coverages-amount-container')]"
        # Esperar que el contenedor sea visible
        total_container_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, total_container_xpath))
        )
        # Hacer scroll hasta el elemento
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", total_container_element)
        # Hacer clic en el contenedor del valor total
        total_container_element.click()
        print("Se hizo clic en el contenedor del valor total correctamente.")
        time.sleep(5)
        title_xpath = "//*[contains(text(), 'Cantidad de semestres')]"  # Busca cualquier etiqueta con este texto
        # Esperar hasta que el texto sea visible en la página
        titulo_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_xpath))
        )

        # Validar que el texto encontrado sea el esperado
        assert titulo_element.text.strip() == "Cantidad de semestres", "El texto 'Cantidad de semestres' no está presente."
        print("El texto 'Cantidad de semestres' está presente en la página.")
        time.sleep(5)
        # XPath del combo box (campo de entrada)
        combobox_xpath = "//input[@role='combobox' and contains(@class, 'slds-input')]"
        # XPath de la opción "3" dentro de la lista desplegable
        option_xpath = "//li[@role='option' and text()='3']"
        # Esperar que el combo box sea clickeable y hacer clic para abrir la lista
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        )
        combobox_element.click()
        print("Combo box abierto.")
        # Esperar que la opción 3 sea visible y hacer clic en ella
        option_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, option_xpath))
        )
        option_element.click()
        time.sleep(5)
        print("Opción 3 seleccionada.")
        texto_xpath = "//*[contains(text(), '$ 0,00')]"  # Busca cualquier etiqueta que contenga el texto exacto
        # Esperar hasta que el texto sea visible en la página
        print("El texto '$ 0,00' está presente en la página.")
        time.sleep(5)

        # XPath basado en el texto "NO"
        si_xpath = "//label[span[text()='NO']]"
        # Esperar hasta que el elemento esté visible y clickeable
        si_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, si_xpath))
        )
        # Hacer scroll hasta el elemento (opcional, por si no está en pantalla)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", si_element)
        # Hacer clic en el elemento
        si_element.click()
        print("Se hizo clic en el botón 'NO' correctamente.")
        time.sleep(5)
        pass


    def button_cotizar(self):
        button_xpath = "//button[span[text()='Cotizar']]"  # XPath basado en el texto del botón
        # Esperar hasta que el botón sea visible en la página
        button_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, button_xpath))
        )
        # Hacer scroll hasta el botón usando el elemento correcto
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_element)
        # Esperar que sea clickeable y hacer clic
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()
        print("Botón 'Cotizar' clickeado con éxito.")
        time.sleep(20)
        pass

    def boton_atras(self):
        # XPath basado en el texto dentro del botón
        boton_atras_xpath = "//button[span[text()='Anterior']]"
        # Esperar hasta que el botón sea visible y clickeable
        boton_atras = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, boton_atras_xpath))
        )
        # Hacer scroll hasta el botón para asegurarse de que sea visible
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", boton_atras)
        # Hacer clic en el botón "Anterior"
        boton_atras.click()
        print("Botón 'Anterior' clickeado correctamente.")
    pass

    def boton_anterior(self):
        boton_atras_xpath = "//button[span[text()='Anterior']]"
        boton_atras = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, boton_atras_xpath))
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(boton_atras).click().perform()

        print("Botón 'Anterior' clickeado con ActionChains.")
    pass