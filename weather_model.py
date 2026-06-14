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