#10 Python Weather Data Collection for Any City
import requests


def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city,
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def display_weather(weather_data):
    try:
        city = weather_data['location']['name']
        temp = weather_data['current']['temp_c']
        weather = weather_data['current']['condition']['text']
        print(f"Weather in {city}: {temp}°C, {weather}")
    except KeyError:
        print("City not found. Please check the name and try again.")


def main():
    api_key = '483a5e42da6a4ba0a9a93429242603'  # Replace with your Weather API key
    city = input("Enter a city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)


if __name__ == "__main__":
    main()