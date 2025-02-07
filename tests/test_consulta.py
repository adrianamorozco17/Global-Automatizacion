import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.consulta_page import ConsultaPage
from pages.form_page import FormPage
from pages.personal_form_page import PersonalFormPage
from pages.financiero_page import FinancieroFormPage
from pages.metas_pages import MetasFormPage

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(service=service, options=options)

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_consulta(driver):
    consulta = ConsultaPage(driver)
    form = FormPage(driver)
    pform = PersonalFormPage(driver)
    finan= FinancieroFormPage(driver)
    metas= MetasFormPage(driver)
    consulta.login()
    form.complete_form()
    form.validate_second_form()
    pform.personal_form()
    finan.perfil_financiero()
    metas.metas_fiancieras()
