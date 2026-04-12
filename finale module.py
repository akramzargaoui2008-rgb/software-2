from flask import Flask, Response
import json

app = Flask(__name__)


def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        n = int(number)
        result = {
            "Number": n,
            "isPrime": is_prime(n)
        }
        return result

    except ValueError:
        response = {
            "message": "Invalid input: please provide an integer",
            "status": 400
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
airports = airportsdata.load()


@app.route('/airport/<icao>')
def airport(icao):
    # ICAO codes are always uppercase
    icao = icao.upper()

    if icao in airports:
        data = airports[icao]
        result = {
            "ICAO": icao,
            "Name": data["name"],
            "Location": data["city"]
        }
        return result
    else:
        response = {
            "message": f"Airport with ICAO code '{icao}' not found",
            "status": 404
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=404, mimetype="application/json")

airports = airportsdata.load()

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)