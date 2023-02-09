import requests

cityName = input("Enter the name of the city: ")

def call(cityName):
    response = requests.get(f"http://0.0.0.0:3000/city/{cityName}")
    return response.text

print(call(cityName))