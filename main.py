from datas import *
from raspage import Scrap
import time
import json

cidades_nomes = [
    'Adamantina', 'Adolfo', 'Aguaí', 'Águas da Prata', 'Águas de Lindóia', 'Águas de Santa Bárbara', 'Águas de São Pedro', 'Agudos', 'Alambari',
    'Alfredo Marcondes', 'Altair', 'Altinópolis', 'Alto Alegre', 'Alumínio', 'Álvares Florence', 'Álvares Machado', 'Álvaro de Carvalho',
    'Alvinlândia', 'Americana', 'Américo Brasiliense', 'Américo de Campos', 'Amparo', 'Analândia', 'Andradina', 'Angatuba', 'Anhembi',
    'Anhumas', 'Aparecida', 'Aparecida d\'Oeste', 'Apiaí', 'Araçariguama', 'Araçatuba', 'Araçoiaba da Serra', 'Aramina', 'Arandu', 'Arapeí',
    'Araraquara', 'Araras', 'Arco-Íris', 'Arealva', 'Areias', 'Areiópolis', 'Ariranha', 'Artur Nogueira', 'Arujá', 'Aspásia', 'Assis',
    'Atibaia', 'Auriflama', 'Avaí', 'Avanhandava', 'Avaré', 'Bady Bassitt', 'Balbinos', 'Bálsamo', 'Bananal', 'Barão de Antonina',
    'Barbosa', 'Bariri', 'Barra Bonita', 'Barra do Chapéu', 'Barra do Turvo', 'Barretos', 'Barrinha', 'Barueri', 'Bastos', 'Batatais',
    'Bauru', 'Bebedouro', 'Bento de Abreu', 'Bernardino de Campos', 'Bertioga', 'Bilac', 'Birigui', 'Biritiba-Mirim', 'Boa Esperança do Sul',
    'Bocaina', 'Bofete', 'Boituva', 'Bom Jesus dos Perdões', 'Bom Sucesso de Itararé', 'Borá', 'Boracéia', 'Borborema', 'Borebi', 'Botucatu',
    'Bragança Paulista', 'Braúna', 'Brejo Alegre', 'Brodowski', 'Brotas', 'Buri', 'Buritama', 'Buritizal', 'Cabrália Paulista', 'Cabreúva',
    'Caçapava', 'Cachoeira Paulista', 'Caconde', 'Cafelândia', 'Caiabu', 'Caieiras', 'Caiuá', 'Cajamar', 'Cajati', 'Cajobi', 'Cajuru',
    'Campina do Monte Alegre', 'Campinas', 'Campo Limpo Paulista', 'Campos do Jordão', 'Campos Novos Paulista', 'Cananéia', 'Canas',
    'Cândido Mota', 'Cândido Rodrigues', 'Canitar', 'Capão Bonito', 'Capela do Alto']



ddd_19 = [
    'Indaiatuba', 'Iracemápolis', 'Itapira', 'Itobi', 'Jaguariúna', 'Leme', 'Limeira', 'Louveira', 'Mococa',
    'Mogi Guaçu', 'Mogi Mirim', 'Monte Mor', 'Nova Odessa', 'Paulínia', 'Pedreira', 'Piracicaba', 'Pirassununga', 'Porto Ferreira',
    'Rafard', 'Rio Claro', 'Rio das Pedras', 'Saltinho', 'Santa Bárbara d\'Oeste', 'Santa Cruz da Conceição', 'Santa Gertrudes', 'Santa Maria da Serra',
    'Santa Rita do Passa Quatro', 'Santo Antônio de Posse', 'Santo Antônio do Jardim', 'São João da Boa Vista', 'São José do Rio Pardo',
    'São Pedro', 'São Sebastião da Grama', 'Serra Negra', 'Socorro', 'Sumaré', 'Tambaú', 'Tapiratiba', 'Torrinha', 'Valinhos',
    'Vargem Grande do Sul', 'Vinhedo'
]

ddd_13 = [
    'Altinópolis', 'Américo Brasiliense', 'Aramina', 'Araraquara', 'Barrinha', 'Batatais', 'Boa Esperança do Sul', 'Borborema',
    'Brodowski', 'Cajuru', 'Cândido Rodrigues', 'Cássia dos Coqueiros', 'Cravinhos', 'Dobrada', 'Dourado', 'Dumont', 'Fernando Prestes',
    'Franca', 'Guariba', 'Guatapará', 'Ibaté', 'Ibitinga', 'Igarapava', 'Ipauçu', 'Itápolis', 'Itirapuã', 'Ituverava', 'Jaboticabal',
    'Jardinópolis', 'Jeriquara', 'Luiz Antônio', 'Matão', 'Miguelópolis', 'Monte Alto', 'Monte Azul Paulista', 'Morro Agudo', 'Motuca',
    'Nova Europa', 'Nuporanga', 'Orlândia', 'Patrocínio Paulista', 'Pedregulho', 'Pitangueiras', 'Pontal', 'Pradópolis', 'Ribeirão Bonito',
    'Ribeirão Corrente', 'Ribeirão Preto', 'Rifaina', 'Rincão', 'Sales Oliveira', 'Santa Cruz da Esperança', 'Santa Ernestina',
    'Santa Lúcia', 'Santa Rosa de Viterbo', 'Santo Antônio da Alegria', 'São Carlos', 'São Joaquim da Barra', 'São José da Bela Vista',
    'São Simão', 'Serra Azul', 'Serrana', 'Sertãozinho', 'Tabatinga', 'Taiaçu', 'Taiúva', 'Taquaral', 'Taquaritinga', 'Trabiju',
    'Vista Alegre do Alto'
]


ddd_17 = [
    'Adolfo', 'Altair', 'Álvares Florence', 'Álvares Machado', 'Alto Alegre', 'Andradina', 'Aparecida d\'Oeste', 'Ariranha', 'Aspásia',
    'Auriflama', 'Avanhandava', 'Bady Bassitt', 'Barbosa', 'Bálsamo', 'Bandeirantes d\'Oeste', 'Bento de Abreu', 'Bilac', 'Birigui',
    'Braúna', 'Brejo Alegre', 'Buritama', 'Cafelândia', 'Caiabu', 'Caiuá', 'Cardoso', 'Castilho', 'Clementina', 'Coroados', 'Cosmorama',
    'Dirce Reis', 'Dolcinópolis', 'Elisiário', 'Embaúba', 'Estrela d\'Oeste', 'Eurípedes da Silva', 'Fernandópolis', 'Florínia',
    'Floreal', 'Flórida Paulista', 'General Salgado', 'Glicério', 'Guaraci', 'Guarani d\'Oeste', 'Guzolândia', 'Ibirá', 'Icém',
    'Indiaporã', 'Inúbia Paulista', 'Ipiguá', 'Irapuã', 'Itajobi', 'Itapura', 'Jaborandi', 'Jaci', 'Jales', 'José Bonifácio',
    'João Ramalho', 'Lavinia', 'Lourdes', 'Lourdes', 'Lucélia', 'Luiziânia', 'Macaubal', 'Macedônia', 'Magda', 'Marapoama',
    'Mariápolis', 'Marinópolis', 'Mesópolis', 'Mira Estrela', 'Mirandópolis', 'Mirassol', 'Mirassolândia', 'Monções', 'Monte Aprazível',
    'Monte Castelo', 'Murutinga do Sul', 'Neves Paulista', 'Nhandeara', 'Nova Aliança', 'Nova Canaã Paulista', 'Nova Castilho',
    'Nova Guataporanga', 'Nova Luzitânia', 'Novais', 'Novo Horizonte', 'Onda Verde', 'Orindiúva', 'Ouroeste', 'Palestina', 'Palmares Paulista',
    'Palmeira d\'Oeste', 'Panorama', 'Paranapuã', 'Parisi', 'Paulicéia', 'Paulo de Faria', 'Pedranópolis', 'Penápolis', 'Pereira Barreto',
    'Piacatu', 'Pirangi', 'Planalto', 'Poloni', 'Pontalinda', 'Pontes Gestal', 'Populina', 'Praia Grande', 'Pracinha', 'Presidente Bernardes',
    'Presidente Epitácio', 'Presidente Prudente', 'Presidente Venceslau', 'Promissão', 'Queiroz', 'Rafard', 'Ribeirão dos Índios',
    'Rubiné'
]




words = {
    'ateliê': ['ateliê', 'atelier', 'design de moda', 'confecção roupas' ],
    'tapeçaria': ['tapeçaria', 'tecedura', 'tecelagem', 'tecelagem de tapetes'],
    'loja de tecidos': ['loja de tecidos', 'casa de tecidos', 'comércio têxtil', 'loja de aviamentos' , 'loja de costura'],
    'loja de retalhos' : ['loja de retalhos', 'tecidos para artesanato', ],
    'artesanato' : ['tecidos de artesanatos', ],
    'alfaiataria' : [' loja de alfaiataria', 'alfaiate']
    
}



word =  ["ateliê", "tapeçaria", "loja de tecidos", 'alfaiate', "loja de retalhos", "tecido artesanato", "alfaiataria", 'loja de costura', 'estamparia']
# word =  ["tapeçaria", "loja de tecidos",]


driver = Scrap()



driver.searchh('valinhos', 'loja tecidos')
for city in ddd_19:

    lojas = []
    for store in word:
        driver.searchh(city, store)
        lojas.append(driver.get_datas())
    
    
    dic = dict({city: lojas})
    json_data = json.dumps(dic, indent=4)
    with open('draftt.json', "w") as outfile:  
        json.dump(dic, outfile, indent=4) 
    
    logs = Log(city)
    logs._draft(json_data)
    dupl = logs._find_duplicated()
    lo = logs.format(duplicated=dupl)
    logs._save(lo)
    
    
    os = True
    if os == True:
        with open('dados.json', "a") as outfile:  
            json.dump(dic, outfile, indent=4) 



time.sleep(20)
        
        
