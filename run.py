import sys
from weather_model import WeatherAppModel

def main():
    """App entry loop handling basic choice validation & clean shutdown patterns."""
    app_data = WeatherAppModel()
    
    while True:
        try:
            display_main_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == "6":
                print("\nThank you for using Weather Dashboard CLI. Goodbye!")
                sys.exit(0)
        except KeyboardInterrupt:
            print("\n\nApplication closing down gracefully...")
            sys.exit(0)

if __name__ == "__main__":
    main()

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