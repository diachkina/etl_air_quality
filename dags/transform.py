import pandas as pd

def transform_data(**kwargs):
    """
    Transforms raw air quality data into a structured and cleaned format.

    This function reads raw JSON data containing air quality measurements and forecasts, 
    processes it into a tabular format, and saves it as a cleaned CSV file.

    Args:
        **kwargs: Arbitrary keyword arguments (not used explicitly in this function).

    Process:
        - Reads the JSON file `/tmp/air_quality55.json` into a Pandas DataFrame.
        - Extracts key attributes such as city, AQI, and the dominant pollutant.
        - Parses pollutant concentration data and daily forecast values for PM2.5 and PM10.
        - Expands forecast data so that each forecasted day has its own row.
        - Fills missing numerical values with the column mean (rounded to 2 decimal places).
        - Saves the cleaned dataset as a CSV file in `/tmp/cleaned_air_quality.csv`.

    Output:
        - A CSV file `/tmp/cleaned_air_quality.csv` containing structured and cleaned data.

    Notes:
        - If forecast data is missing for a city, it will not be included in the final dataset.
        - Numeric columns with NaN values are replaced by their respective column mean.
    """


    with open('/tmp/air_quality.json', 'r', encoding='utf-8') as f:
        data = pd.read_json(f)

    rows = []
    for record in data.to_dict(orient='records'):
        city = record['city']
        aqi = record['data']['aqi']
        dominant_pollutant = record['data']['dominentpol']
    
        parameters = {param.upper(): value['v'] for param, value in record['data']['iaqi'].items()}
    
        forecast_data = record['data'].get('forecast', {}).get('daily', {})
    
        for forecast_day in forecast_data.get('pm25', []):
            forecast_pm10 = next((x for x in forecast_data.get('pm10', []) if x['day'] == forecast_day['day']), {})

            row = {
                'City': city,
                'AQI': aqi,
                'Dominant Pollutant': dominant_pollutant,
                'Date': forecast_day['day'],
                **parameters,
                'PM2.5 Forecast (Avg)': forecast_day.get('avg'),
                'PM2.5 Forecast (Min)': forecast_day.get('min'),
                'PM2.5 Forecast (Max)': forecast_day.get('max'),
                'PM10 Forecast (Avg)': forecast_pm10.get('avg'),
                'PM10 Forecast (Min)': forecast_pm10.get('min'),
                'PM10 Forecast (Max)': forecast_pm10.get('max'),
            }
            rows.append(row)

    df = pd.DataFrame(rows)

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(round(df[numeric_cols].mean(), 2))

    df.to_csv('/tmp/cleaned_air_quality.csv', index=False, encoding='utf-8')

