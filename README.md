# Flight Data Management System

This system fetches and manages flight data from multiple Vietnamese airlines using the Aviation Stack API.

## Setup

### Prerequisites
- Python 3.x
- MySQL Database
- Required Python packages:
  ```bash
  pip install requests mysql-connector-python
  ```

### Database Configuration
Make sure you have MySQL installed and configured with:
- Host: localhost
- Username: minhtb
- Password: 1403
- Database: flight

## Usage

### 1. Fetch Flight Data
Run the getData script to fetch flight data from multiple airlines:

```bash
python getData.py
```
This will create JSON files for each airline:
- bamboo_airways_flights.json
- vietnam_airlines_flights.json
- vietjet_air_flights.json
- pacific_airlines_flights.json

### 2. Push

```bash
python pushData.py

```

## Data Structure

### Airlines Table
- airline_id: Primary Key
- name: Airline Name
- code: Airline Code
- country: Country of Origin
- created_at: Creation Timestamp
- updated_at: Last Update Timestamp

### Flights Table
- airline_id: Foreign Key to Airlines
- flight_number: Flight IATA Code
- departure_airport: Departure Airport IATA Code
- arrival_airport: Arrival Airport IATA Code
- departure_time: Scheduled Departure Time
- arrival_time: Scheduled Arrival Time
- status: Flight Status
- economy_price: Economy Class Price
- business_price: Business Class Price
- first_class_price: First Class Price
- available_seats: Number of Available Seats

## API Configuration
- API Provider: Aviation Stack
- Base URL: https://api.aviationstack.com/v1/flights
- Access Key: Required for API calls

## Airlines Covered
1. Vietnam Airlines (ID: 3)
2. Vietjet Air (ID: 4)
3. Bamboo Airways (ID: 5)
4. Vietravel Airlines (ID: 6)
