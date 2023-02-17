# import requests

# def search_car_model(make):
#     url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         models = data['Results']
#         print('Modelos de carros para a marca', make)
#         for model in models:
#             print(model['Model_Name'])
#     else:
#         print('Erro ao fazer a solicitação à API')

# make = input('Digite a marca de carro que deseja pesquisar: ')
# search_car_model(make)

import requests

def get_car_info(make, model, year):
    url = f'https://one.nhtsa.gov/webapi/api/SafetyRatings/modelyear/{year}/make/{make}/model/{model}?format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for item in data['Results']:
            print(f"Ano do modelo: {item['ModelYear']}")
            print(f"Marca: {item['Make']}")
            print(f"Modelo: {item['Model']}")
            print(f"Tipo de veículo: {item['VehicleType']}")
            print(f"Classificação de segurança: {item['OverallRating']}")
    else:
        print('Erro ao fazer a solicitação à API')

make = input('Digite a marca do carro: ')
model = input('Digite o modelo do carro: ')
year = input('Digite o ano do modelo: ')

get_car_info(make, model, year)