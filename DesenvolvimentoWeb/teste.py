# import logging

# # CRITICAL
# # ERROR
# # WARNING
# # INFO
# # DEBUG

# logging.basicConfig(level=logging.DEBUG, filename='log.log', format='%(levelname)s : %(asctime)s : %(message)s')


# nota = 10


# if nota < 5:
#     logging.critical('Reprovado')

# elif nota >= 5:
#     logging.info('Aprovado')

# import requests

# # Solicita ao usuário que digite o nome da cidade
# cidade = input("Digite o nome da cidade: ")

# # Faz uma solicitação à API de previsão do tempo para a cidade especificada pelo usuário
# response = requests.get(f'https://weather.contrateumdev.com.br/api/weather/city/?city={cidade}').json()

# print (response)

# # Extrai os dados da resposta JSON
# city_name = response['name']
# temp_max = response['main']['temp_max']
# temp_min = response['main']['temp_min']

# # Exibe os dados na tela
# print(f"Previsão do tempo para {city_name}:")
# print(f"Temperatura máxima: {temp_max}°C")
# print(f"Temperatura mínima: {temp_min}°C")

import requests

marca = input('Digite a marca da moto: ')
response = requests.get(f'https://parallelum.com.br/fipe/api/v1/motos/marcas').json()
print(response)
