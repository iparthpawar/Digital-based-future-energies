import requests

# API endpoint, API key, location, and parameters
api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'your_api_key'
location = 'New York'
params = {
    'q': location,
    'appid': api_key,
    'units': 'metric'
}

# Send GET request to API endpoint with specified parameters
response = requests.get(api_endpoint, params=params)

# Check if API call was successful
if response.ok:
    # Parse JSON data from response
    data = response.json()

    # Extract relevant weather information from parsed data
    temperature = data.get('main', {}).get('temp')
    description = data.get('weather', [{}])[0].get('description')
    wind_speed = data.get('wind', {}).get('speed')

    # Check if required data is present and valid
    if temperature is not None and description is not None and wind_speed is not None:
        # Print out weather information
        print(f'Current weather in {location}:')
        print(f'Temperature: {temperature}°C')
        print(f'Description: {description}')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print('Error: Required weather data not found or invalid')
else:
    # If API call was unsuccessful, print error message with status code
    print(
        f'Error: Failed to retrieve data, status code: {response.status_code}')
    
    