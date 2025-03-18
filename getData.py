import requests
import json

# API configuration
BASE_URL = "https://api.aviationstack.com/v1/flights"
ACCESS_KEY = ""

# List of airlines to fetch data for
airlines = [
    "bamboo airways",
    "vietnam airlines",
    "vietjet air",
    "vietravel airlines"
]

def fetch_airline_data(airline_name):
    params = {
        'access_key': ACCESS_KEY,
        'airline_name': airline_name
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Get the JSON data
        data = response.json()
        
        # Save to file
        filename = f"{airline_name.replace(' ', '_')}_flights.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
        print(f"Successfully fetched and saved data for {airline_name}")
        print(f"Total flights found: {data.get('pagination', {}).get('total', 0)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {airline_name}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON for {airline_name}: {e}")

def main():
    print("Starting to fetch flight data...")
    
    for airline in airlines:
        print(f"\nFetching data for {airline}...")
        fetch_airline_data(airline)
        
    print("\nData collection completed!")

if __name__ == "__main__":
    main()
