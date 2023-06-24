# create a method named "get_weather_forecast" that takes "city" as an argument

# import the requests library
import requests
import json
import sys

def get_weather_forecast(city):
    api_key = "887fe186a3b285652bf8857fa8be93f2"  # Replace with your OpenWeatherMap API key
    base_url = "https://openweathermap.org/data/2.5/find"  # API endpoint for "weather forecast"

    # Create the API request URL
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
#
#     # Make the request
#create a try-except block
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract relevant weather data
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    except json.JSONDecodeError:
        print("Error: Failed to parse response from the API.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of a city.")
    else:
        city_name = " ".join(sys.argv[1:])
        get_weather_forecast(city_name)
