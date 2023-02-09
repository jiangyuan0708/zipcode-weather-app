from flask import Flask, request
import requests


app = Flask(__name__)

zipcodes = {
    'Sunnyvale': '94089',
    'MountainView': '94043',
    'Fremont': '94535'
}

@app.route('/city/<cityName>')
def zipcode(cityName):
    if cityName in zipcodes:
        zip = zipcodes[cityName]
        response = requests.get(f"http://172.17.0.2:3001/weather/{zip}")
        return response.text
    else:
        return f"The zip code of the city: {cityName} is not available."    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)