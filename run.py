import os
import sys
from dotenv import load_dotenv
from weather_model import WeatherAppModel
from api_handler import fetch_weather_by_city

# Load the hidden local .env file variables into the system
load_dotenv()

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

# Define all helper functions BEFORE they are called

def print_divider():
    """Prints a consistent visual divider fitting the 80-char mock terminal."""
    print("-" * 65)


def display_main_menu():
    """Displays standard choices on the console interface."""
    print_divider()
    print("                WEATHER DASHBOARD CLI")
    print_divider()
    print("1. Check Current Weather for a City")
    print("2. View Favorite Cities")
    print("3. Add City to Favorites")
    print("4. Remove City from Favorites")
    print("5. View Search History Log")
    print("6. Exit Application")
    print_divider()


def handle_view_favorites(model):
    """Lists current favorite items saved inside the model instance."""
    favorites = model.get_favorites()
    print("\n--- Your Favorite Cities ---")
    if not favorites:
        print("Your favorites list is currently empty.")
    else:
        for index, city in enumerate(favorites, start=1):
            print(f"{index}. {city}")


def handle_add_favorite(model):
    """Captures and validates a new city item to include in favorites collection."""
    print("\n--- Add a Favorite City ---")
    city_input = input("Enter city name to add: ").strip()

    if not city_input or city_input.isdigit():
        print("Error: Please provide a valid textual city identifier.")
        return

    if model.add_favorite(city_input):
        print(f"Success: '{city_input.title()}' has been added.")
    else:
        print(f"Notice: '{city_input.title()}' is already in your favorites.")


def handle_weather_lookup(model):
    """Prompts for city input, handles validation, and presents results."""
    print("\n--- Current Weather Lookup ---")
    city_input = input("Enter city name: ").strip()

    if not city_input:
        print("Error: Input cannot be empty. Please enter a valid name.")
        return

    print(f"Fetching data for '{city_input}'...")
    result = fetch_weather_by_city(city_input, API_KEY)

    if result["success"]:
        print_divider()
        print(f"Weather for: {result['city']}, {result['country']}")
        print(f"Temperature: {result['temp']}°C")
        print(f"Humidity:    {result['humidity']}%")
        print(f"Conditions:  {result['condition']}")
        print_divider()

        model.add_to_history(
            result["city"], result["temp"], result["condition"])
    else:
        print(f"Error: {result['message']}")


def handle_remove_favorite(model):
    """Provides removal access over persistent local business models."""
    print("\n--- Remove a Favorite City ---")
    city_input = input("Enter city name to remove: ").strip()

    if not city_input:
        print("Error: Input cannot be empty.")
        return

    if model.remove_favorite(city_input):
        print(f"Success: '{city_input.title()}' removed from favorites.")
    else:
        print(f"Error: '{city_input.title()}' was not found in favorites.")


def handle_view_history(model):
    """Iterates and displays local program logging models."""
    history = model.get_history()
    print("\n--- Local Search History Log ---")
    if not history:
        print("No queries recorded during this application session.")
    else:
        for index, entry in enumerate(history, start=1):
            print(
                f"[{index}] {entry['city']} | {entry['temp']}°C | {entry['condition']}")

# Define main() after all the helper functions it relies on


def main():
    """App entry loop handling basic choice validation & clean shutdown patterns."""
    app_data = WeatherAppModel()

    while True:
        try:
            display_main_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                handle_weather_lookup(app_data)
            elif choice == "2":  # FIXED: Changed 'if' to 'elif' here to maintain the logic chain
                handle_view_favorites(app_data)
            elif choice == "3":
                handle_add_favorite(app_data)
            elif choice == "4":
                handle_remove_favorite(app_data)
            elif choice == "5":
                handle_view_history(app_data)
            elif choice == "6":
                print("\nThank you for using Weather Dashboard CLI. Goodbye!")
                sys.exit(0)
            else:
                # ADDED: A fallback if the user types something like "7" or "abc"
                print("\nInvalid entry. Please choose a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nApplication closing down gracefully...")
            sys.exit(0)


# Execution trigger at the absolute bottom
if __name__ == "__main__":
    main()
