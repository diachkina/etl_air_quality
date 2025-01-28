import requests
import pandas as pd
import json

def extract_data(**kwargs):
    """
    Extracts air quality data for a list of cities using the WAQI API.

    This function sends requests to the WAQI API for multiple cities, retrieves 
    air quality data, and saves the extracted data as a JSON file.

    Args:
        **kwargs: Arbitrary keyword arguments (not used explicitly in this function).

    Process:
        - Defines a list of cities to query.
        - Constructs API requests using the base URL and API key.
        - Sends GET requests to the API for each city.
        - Checks if the response is valid (status code 200 and 'ok' status).
        - Extracts the relevant air quality data for each city.
        - Saves the collected data into a JSON file in the `/tmp/` directory.

    Output:
        - A JSON file `/tmp/air_quality55.json` containing air quality data for 
          the specified cities.

    Notes:
        - Ensure that the API key is valid and has sufficient request limits.
        - The function does not return any values but writes data to a file.
    """

    
    api_key = 'ea7eacb87a775d6b2bf8a652e1c970de11365860'
    cities = ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven', 
              'Groningen', 'Breda', 'Maastricht', 'Delft', 'Arnhem']
    base_url = 'https://api.waqi.info/feed/{city}/?token={api_key}'
    all_data = []

    for city in cities:
        url = base_url.format(city=city, api_key=api_key)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'ok':
                all_data.append({'city': city, 'data': data['data']})

    with open('/tmp/air_quality.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)