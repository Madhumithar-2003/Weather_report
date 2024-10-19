import requests
from datetime import datetime

def get_weather():
    api_key = "183ed11f5206e8d7fef2076e86b42f59"
    location=input("Enter your location: ")

    # Construct final URL
    complete_url =f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    # Send request and get response
    response = requests.get(complete_url)
    
    # Parse JSON response
    data = response.json()

    # Check if the city is found
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        # Extract and display weather details
        temperature = (main["temp"] - 273.15)
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print(f"location: {location}")
        print(f"Date & Time: {date_time}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
    else:
        print("location not found!")



get_weather()
