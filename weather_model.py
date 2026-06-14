class WeatherAppModel:
    """Manages internal app state data including search metrics and favorites."""
    def __init__(self):
        self.search_history = []
        self.favorites = set()