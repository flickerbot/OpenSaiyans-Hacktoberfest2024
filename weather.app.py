import requests

def get_weather(city_name, api_key):
    # URL to fetch the weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant information
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Print the weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)
