from flask import Flask, request

app = Flask(__name__)

zip_code_to_weather = {94089: "Sunny", 94538: "Rainy", 94043: "Windy"}

@app.route('/weather/<int:id>')
def weather(id):
    if id in zip_code_to_weather:
        return f"The weather in the area (zipcode: {id}) is {zip_code_to_weather[id]}."
    else:
        return f"The weather in the area (zipcode: {id}) is not available."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)