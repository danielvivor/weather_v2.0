import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather_by_city(city_name, api_key):
    """Fetches real-time weather data for a specified city string."""
    if not api_key or api_key == "YOUR_ACTUAL_API_KEY_HERE":
        return {"success": False, "message": "API Key configuration missing."}

    params = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code == 404:
            return {"success": False, "message": f"City '{city_name}' not found."}

        response.raise_for_status()
        data = response.json()
        return {
            "success": True,
            "city": data.get("name"),
            "country": data.get("sys", {}).get("country"),
            "temp": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "condition": data.get("weather", [{}])[0].get("description", "N/A").capitalize()
        }
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": f"Network error occurred: {e}"}
