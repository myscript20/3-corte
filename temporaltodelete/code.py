import json

with open('cars.json', 'r') as archivo:
    car = json.load(archivo)

for año, carro in car["años"].items():
    print(año)
    for auto in carro:
        print(auto["modelo"])
        