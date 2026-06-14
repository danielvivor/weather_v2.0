class WeatherAppModel:
    """
    Manages the core application data, including user search history
    and a collection of favorite cities.
    """
    def __init__(self):
        # A list to store dictionaries of past successful weather queries
        self.search_history = []
        # A set to maintain unique favorite cities
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

    def remove_favorite(self, city):
        """Removes a city from favorites. Returns True if removed successfully."""
        normalized_city = city.strip().title()
        if normalized_city in self.favorites:
            self.favorites.remove(normalized_city)
            return True
        return False

    def get_history(self):
        """Returns the search history records."""
        return self.search_history

    def get_favorites(self):
        """Returns a sorted list of favorite cities."""
        return sorted(list(self.favorites))