import json
from collections import Counter
import datetime
import time

data = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}

with open('dados.json', 'w') as file:
    json.dump(data, file)
    
    
    
    
codigo_cor = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'magenta': '\033[95m',
        'ciano': '\033[96m',
        'reset': '\033[0m'
    } 
    

class Log:
    
    def __init__(self, city, obs=None):
        self.city = city
        self.initial_time = datetime.datetime.now().isoformat()
        self.obs = obs
    
    
    def _draft(self, logs):
        with open('draft.json', 'w') as file:
            json.dump(logs, file, indent=4, ensure_ascii=False)   
    
    
    
    def format(self, *errors, duplicated=None):
        times = str(self.initial_time) + '//' + str(datetime.datetime.now().isoformat())
        print(times)
        text = str(self.city + '\033[91m'), duplicated, str(errors) + '\n\n'
        return (text, times)
        
        
    def _find_duplicated(self):
        with open('draftt.json', 'r') as arquivo:
            codigo = arquivo.read()
            termos = codigo.split()  # Divide o código em termos individuais
            contador = Counter(termos)  # Conta a ocorrência de cada termo

            duplicados = [termo for termo, quantidade in contador.items() if quantidade > 1]

        return duplicados
    
    def _save(self, logs):
        with open('log.txt', 'a') as file:
            json.dump(logs, file)    

    def _delete(self):
        ...




                                                                                                                                                                                              