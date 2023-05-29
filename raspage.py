from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import *
from selenium.webdriver.chrome.service import Service
import time



# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service = servico)



# //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div

# //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]/div


# //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]/div

# //*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/button/div/div[3]/div[1]

# //*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[5]/button/div/div[3]/div[1]


# //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]

# //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]




# pesquisa seletor
##APjFqb
# pesquisa xpath
# //*[@id="APjFqb"]


# class="Nv2PK THOPZb CpccDe "





# Configurar o caminho para o driver do Chrome
# driver_path = 'caminho/para/o/chromedriver.exe'

# Inicializar o driver do Chrome
# driver = webdriver.Chrome(driver_path)

# Acessar o site desejado
# driver.get('https://www.exemplo.com')



# navegador.get('https://www.google.com')

# time.sleep(3)


# # user_element = navegador.find_element("xpath", '//*[@id="APjFqb"]')
# # user_element.clear()
# # user_element.send_keys('casa')

# def searchh(city, store):
#         statement = f'{store} em {city}'
#         statement = str(statement.replace(' ', '+'))
#         print(statement)
#         test = 'https://www.google.com.br/maps/search/' + statement
#         print(type(test))
#         navegador.get(test)
        
# searchh('valinhos', 'tecelagem')



# time.sleep(78)



# Localizar o elemento desejado pelo seletor CSS
# elemento = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'seletor-css-do-elemento'))
# )

# # Clicar no elemento
# elemento.click()

# Fechar o navegador




# navegador.quit()

selectors = {
            "search_box": '//*[@id="APjFqb"]',
            "search_button": '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]',
            'maps_button': '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a',
            'fone' : lambda number :  '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]'.replace('term', number)
               
            
    }

        
class Scrap:
    pula = '\n\n\n\n'
        
    def __init__(self):
        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = servico)
             
        
    def search(self, city, store):
        statement = f'{store} em {city}'
        box = self.driver.find_element("xpath", selectors["search_box"])
        box.clear()
        box.send_keys(statement)
        self.driver.find_element("xpath", selectors["search_button"]).click()        
        
        
    def go_google(self):
        self.driver.get('https://www.google.com')
        
        
    def searchh(self, city, store):
        statement = f'{store} em {city}'
        statement = str(statement.replace(' ', '+'))
        self.driver.get(('https://www.google.com.br/maps/search/' + statement))
        
        
        
        
    def _format_xpath(self, n):
        xpath_phone = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{n}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]'
        xpath_name = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{n}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]'
        return xpath_name, xpath_phone
        
    def get_datas(self):

        n = 1
        place_name = []
        place_phone = []
        
        while n < 20:
            xpath_name, xpath_phone = self._format_xpath(n)
            print('paaaaaaaaaaaaaaaaaaaaaaau', n, self.pula)
            
            try:
                place_name.append(self.driver.find_element("xpath", xpath_name).text)
                place_phone.append(self.driver.find_element("xpath", xpath_phone).text)
                print(place_name, place_phone)
            
            except Exception as e:
                print(e, self.pula)
                
                
                
            n = n + 1
            
        
        return dict(zip(place_name, place_phone))
            
            
        
        
        
# sssssadaaaaaaaaaa //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]

# ssssssssssssssaa //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]
# sssssssssssssss '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]'
# xpath_phone = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div{n}/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]'
# xpath_name = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div{n}/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]'
