from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#abrir navedador
navegador = webdriver.Chrome()

#acessar site
navegador.get("https://www.hashtagtreinamentos.com/")

#navegador em tela cheia
navegador.maximize_window()

#teste de click no botao verde
#botao_verde = navegador.find_element("class name", "botao-verde")
# Faz scroll até o botão (coloca ele no centro da tela)
#navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_verde)
#time.sleep(2)
#botao_verde.click()

#############################################################################################

#selecionando o componente quando se tem a mesma classe em varios componentes
# botao_assinatura = navegador.find_elements("class name", "header__titulo")

# for botao in botao_assinatura:
#     if "Assinatura" in botao.text:
#         botao.click()
#         break        

# time.sleep(10)

#####################################################################################################

#gerenciando as abas do navegador

botao_verde = navegador.find_element("class name", "botao-verde")

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_verde)
time.sleep(2)
botao_verde.click()

#selecionando a aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

#navegando para um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

navegador.find_element("id", "firstname").send_keys("Alex Rangel")
navegador.find_element("id", "email").send_keys("teste@teste.com")
navegador.find_element("id", "phone").send_keys("21999999999")

botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

#dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_quero_clicar)

#opção 1 (espera manual)
time.sleep(3)

#opção 2 (espera dinamica)


#espera = WebDriverWait(navegador,100)
#espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()


time.sleep(5)

