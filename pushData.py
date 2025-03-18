import json
import mysql.connector
from mysql.connector import Error
import random

# Read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'minhtb',
    'password': '1403',
    'database': 'flight'
}

# List of JSON files to process with their corresponding airline IDs
json_files = [
    ('bamboo_airways_flights.json', 5),
    ('vietnam_airlines_flights.json', 3),
    ('vietjet_air_flights.json', 4),
    ('vietravel_airlines_flights.json', 6)
]

try:
    # Establish database connection
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Prepare SQL query
        insert_query = """
        INSERT INTO flights
        (airline_id, flight_number, departure_airport, arrival_airport, 
         departure_time, arrival_time, status, economy_price, business_price, first_class_price, available_seats)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        total_flights_inserted = 0
        
        # Process each JSON file
        for json_file, airline_id in json_files:
            try:
                print(f"\nProcessing {json_file}...")
                
                # Read JSON data
                json_data = read_json_file(json_file)
                
                # Access the 'data' array from the JSON
                flights = json_data['data']
                
                flights_in_file = 0
                
                # Process each flight in the data array
                for flight in flights:
                    values = (
                        airline_id,  # Use the fixed airline_id for each file
                        flight['flight']['iata'],
                        flight['departure']['iata'],
                        flight['arrival']['iata'],
                        flight['departure']['scheduled'],
                        flight['arrival']['scheduled'],
                        'on-time',
                        random.randint(250, 410),
                        random.randint(750, 900),
                        random.randint(1000, 1500),
                        random.randint(100, 150),
                    )
                    
                    # Execute the insert query
                    cursor.execute(insert_query, values)
                    flights_in_file += 1
                
                print(f"Successfully inserted {flights_in_file} flights from {json_file}")
                total_flights_inserted += flights_in_file
                
            except FileNotFoundError:
                print(f"Warning: Could not find {json_file}")
            except KeyError as e:
                print(f"Error: Invalid data structure in {json_file}: {e}")
        
        # Commit the changes
        connection.commit()
        print(f"\nTotal flights inserted successfully: {total_flights_inserted}")

except Error as e:
    print(f"Database Error: {e}")

finally:
    # Close database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed")
