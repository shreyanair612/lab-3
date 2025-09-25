import requests

# WeatherAPI key
WEATHER_API_KEY = 'afec3c7640a245b696151928252509'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(url)

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = response.json()

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"{data['location']['name']}, {data['location']['region']}")
        print(f"  Temperature: {data['current']['temp_f']}°F. Feels like {data['current']['feelslike_f']}°F")
        print(f"  It's currently {data['current']['condition']['text']}. Humidity: {data['current']['humidity']}%")
        print(f"  Wind: {data['current']['wind_mph']} mph {data['current']['wind_dir']}")
        print(f"  Atmospheric Pressure: {data['current']['pressure_mb']} mb.")
        print(f"  UV Index: {data['current']['uv']}")
        print(f"  Cloud Cover: {data['current']['cloud']}%")
        print(f"  Visibility: {data['current']['vis_miles']} mi")
    elif response.status_code == 400:
        print("Bad Request: The city name may be missing/invalid.")
    elif response.status_code == 401:
        print("Unauthorized: Your API key is missing/incorrect.")
    elif response.status_code == 404:
        print("Not found: Your city was not found. Check spelling.")
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter city name (ex: Los Angeles): ")
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
    pass
