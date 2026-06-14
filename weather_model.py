class WeatherAppModel:
    """Manages internal app state data including search metrics and favorites."""
    def __init__(self):
        self.search_history = []
        self.favorites = set()

def add_to_history(self, city, temperature, condition):
        """Adds a successful query's key metrics to the history log."""
        record = {
            "city": city.title(),
            "temp": temperature,
            "condition": condition
        }
        self.search_history.append(record)

def add_favorite(self, city):
        """Adds a city to the favorites collection. Returns True if added."""
        normalized_city = city.strip().title()
        if normalized_city and normalized_city not in self.favorites:
            self.favorites.add(normalized_city)
            return True
        return False