# biblioteca jason para transformar um objeto em dicionário
import json

# a biblioteca PANDAS serve para trabalhar com dados em CSV
# a nomenclatura "as pd" serve para transformar o nome um pequeno atalho.Nesse caso ao inves de chamar "pandas",  estaremos chamando "pd" somente e a biblioteca sera acionada
import pandas as pd

import requests
# a biblioteca request sera utilizada para fazer requisiçoes a um determinado servidor
#  para instalar a biblioteca, digitar no prompt de comando o seguinte comando: pip install requests

# iremos utilizar os dados da api do site fixer.io para acompanhar o cambio das moedas globais
# o endereço da url foi fornecido após cadastro no site
url = "http://data.fixer.io/api/latest?access_key=a88e5172c7cc3ff6d8322073432c233d"

# apresenta uma mensagem para dar a sensação que está funcionando
print("Acessando base de dados...")
print(" ")
# Fazer requisição ao site
response = requests.get(url)
if response.status_code == 200:
    print("Conseguiu acessar a base de dados!")
    print(" ")
    print("Buscando informações das moedas...")
    print(" ")
    
    # comando para  
    dados = response.json()
    day = dados['date']
    print("Acessando dados do dia %s/%s/%s" % (day[8:], day[5:7], day[0:4]))

    # conversão das moedas escolhidas no dicionário para BRL fazendo TAXA DO REAL / TAXA DA MOEDA ESCOLHIDA
    euro_real = round (dados['rates']['BRL'] / dados['rates']['EUR'], 2)
    dollar_real = round (dados['rates']['BRL'] / dados['rates']['USD'], 2)
    btc_real = round (dados['rates']['BRL'] / dados['rates']['BTC'], 2)

    # mostra os valores de euro, dollar e btc em real
    print(" ")
    print("1 EUR está valendo R$%.2f" % euro_real)
    print("1 USD está valendo R$%.2f" % dollar_real)
    print("1 BTC está valendo R$%.2f" % btc_real)
    df = pd.DataFrame({'Moedas':['Euro','Dolar', 'Bitcoin'], 'Valores':[euro_real, dollar_real, btc_real]})
    df.to_csv("valores.csv", index=False, sep=";")
    print(" ")
    print("O arquivo foi exportado com sucesso para a pasta do projeto")
else:
    print("Site com problemas")