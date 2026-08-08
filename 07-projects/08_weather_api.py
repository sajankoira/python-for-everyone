"""
PROJECT 8: Weather App (API) - Uses requests
To run: pip install requests
Get free API key from openweathermap.org (optional, demo uses mock if no key)
"""

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("requests not installed. Run: pip install requests")
    print("Running demo with mock data")

def get_weather_mock(city):
    # Mock data when no API key or no internet
    mock = {
        "Belagavi": {"temp": 28, "desc": "Partly cloudy", "humidity": 65},
        "Pune": {"temp": 30, "desc": "Sunny", "humidity": 50},
        "Mumbai": {"temp": 32, "desc": "Humid", "humidity": 80},
    }
    return mock.get(city, {"temp": 25, "desc": "Clear", "humidity": 60})

def get_weather_real(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        if res.status_code == 200:
            return {
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            print(f"API Error: {data.get('message','Unknown')}")
            return None
    except Exception as e:
        print(f"Network error: {e}")
        return None

def main():
    print("🌤️ Weather App")
    city = input("Enter city (Belagavi/Pune/Mumbai): ") or "Belagavi"
    
    # If user has API key, use real, else mock
    api_key = input("Enter OpenWeatherMap API key (press Enter for demo mock): ").strip()
    
    if api_key and HAS_REQUESTS:
        weather = get_weather_real(city, api_key)
    else:
        print("(Using demo data - add API key for real data)")
        weather = get_weather_mock(city)

    if weather:
        print(f"\n--- Weather in {city} ---")
        print(f"Temperature: {weather['temp']}°C")
        print(f"Description: {weather['desc']}")
        print(f"Humidity: {weather['humidity']}%")
        # Advice
        if weather['temp'] > 30:
            print("Advice: Stay hydrated! 🥤")
        elif weather['temp'] < 20:
            print("Advice: Carry jacket! 🧥")
        else:
            print("Advice: Nice weather! 😊")

if __name__ == "__main__":
    main()
