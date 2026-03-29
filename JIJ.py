import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke = response.json()
        print(joke["value"])
    else:
        print("Couldn't fetch a joke right now.")
except requests.exceptions.RequestException:
    print("Request could not be completed.")

import requests

API_KEY = "your_api_key"

city = input("Enter city name: ")

request_url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}"
)

try:
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        print(f"Weather: {description}")
        print(f"Temperature: {temp_celsius:.1f} °C")
    elif response.status_code == 404:
        print("City not found. Check the spelling and try again.")
    else:
        print(f"Error: received status code {response.status_code}")
except requests.exceptions.RequestException:
    print("Request could not be completed.")