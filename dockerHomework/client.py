import requests

cityName = input("Enter the name of the city: ")

def call(cityName):
    response = requests.get(f"http://0.0.0.0:3000/city/{cityName}")
    if "not available" in response.text:
        return "The zip code of the city is not available."
    else:
        zip = int(response.text.split(" ")[-1][:-1])

    response = requests.get(f"http://0.0.0.0:3001/weather/{zip}")
    return response.text

print(call(cityName))