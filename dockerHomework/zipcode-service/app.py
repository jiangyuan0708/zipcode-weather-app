from flask import Flask, request


app = Flask(__name__)

zipcodes = {
    'Sunnyvale': '94089',
    'MountainView': '94043',
    'Fremont': '94535'
}

@app.route('/city/<cityName>')
def zipcode(cityName):
    if cityName in zipcodes:
        return f"The zip code of the city: {cityName} is {zipcodes[cityName]}."
    else:
        return f"The zip code of the city: {cityName} is not available."    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)