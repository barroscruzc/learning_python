# Recebe um valor em reais e o converte para dólares segundo a cotação cambial atual,
# utilizando conceitos básicos de API

import requests

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)

dados = req.json()

print(' ' * 10, 'COTAÇÃO DÓLAR')
print('--' * 20)
valor_reais = float(input('Informe o valor em R$ a ser convertido:\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem US${(valor_reais/cotacao):.2f}')
