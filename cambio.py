# biblioteca jason para transformar um objeto em dicionário
import json
import requests
# a biblioteca request sera utilizada para fazer requisiçoes a um determinado servidor
#  para instalar a biblioteca, digitar no prompt de comando o seguinte comando: pip install requests

# iremos utilizar os dados da api do site fixer.io para acompanhar o cambio das moedas globais
# o endereço da url foi fornecido após cadastro no site
url = "http://data.fixer.io/api/latest?access_key=a88e5172c7cc3ff6d8322073432c233d"

# apresenta uma mensagem para dar a sensação que está funcionando
print("Acessando base de dados...")

# Fazer requisição ao site
response = requests.get(url)
if response.status_code == 200:
    print("Conseguiu acessar a base de dados!")
    print("Buscando informações das moedas...")
    
    # comando para  
    dados = response.json()

    # conversão das moedas escolhidas no dicionário para BRL fazendo TAXA DO REAL / TAXA DA MOEDA ESCOLHIDA
    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']

    # mostra os valores de euro, dollar e btc em real
    print("1 EUR está valendo R$%.2f" % euro_real)
    print("1 USD está valendo R$%.2f" % dollar_real)
    print("1 BTC está valendo R$%.2f" % btc_real)
else:
    print("Site com problemas")