import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def plot_aqi():
    """
    Generates and saves a bar chart of AQI (Air Quality Index) for cities.

    The function reads cleaned air quality data from a CSV file and plots the AQI values
    for different cities in the dataset.
    
    Output:
        - Saves the AQI plot as 'aqi_plot.png'.
    """
    df = pd.read_csv('/tmp/cleaned_air_quality.csv')

    plt.figure(figsize=(10, 6))
    plt.bar(df['City'], df['AQI'], color='skyblue')
    plt.title('Air Quality Index (AQI) in Dutch Cities', fontsize=14)
    plt.xlabel('Cities', fontsize=12)
    plt.ylabel('AQI', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('/tmp/aqi_plot.png')
    print('AQI plot saved as "/tmp/aqi_plot.png".')

def plot_pm25_forecast():
    """
    Generates and saves a line plot for PM2.5 forecast trends across cities.

    The function reads cleaned air quality data and plots the average PM2.5 forecast 
    for different cities over time.

    Output:
        - Saves the PM2.5 forecast plot as 'pm25_forecast_plot.png'.
    """
    df = pd.read_csv('/tmp/cleaned_air_quality.csv')

    plt.figure(figsize=(10, 6))
    for city in df['City'].unique():
        city_data = df[df['City'] == city]
        if not city_data['PM2.5 Forecast (Avg)'].isnull().all():
            plt.plot(city_data.index, city_data['PM2.5 Forecast (Avg)'], marker='o', label=city)
    
    plt.title('PM2.5 Forecast in Dutch Cities', fontsize=14)
    plt.xlabel('Days (Index)', fontsize=12)
    plt.ylabel('PM2.5 (μg/m³)', fontsize=12)
    plt.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('/tmp/pm25_forecast_plot.png')
    print('PM2.5 forecast plot saved as "/tmp/pm25_forecast_plot.png".')

def plot_correlation():
    """
    Generates and displays a heatmap of correlations between real air quality parameters.

    This function reads cleaned air quality data, filters out forecasted values, 
    and computes a correlation matrix for actual measurements.

    Output:
        - Displays a correlation heatmap.
    """
    df = pd.read_csv('/tmp/cleaned_air_quality.csv')

    # Exclude forecast columns
    exclude_columns = ['PM2.5 Forecast (Avg)', 'PM2.5 Forecast (Min)', 'PM2.5 Forecast (Max)',
                       'PM10 Forecast (Avg)', 'PM10 Forecast (Min)', 'PM10 Forecast (Max)']
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    numeric_cols_filtered = [col for col in numeric_cols if col not in exclude_columns]

    correlation_matrix = df[numeric_cols_filtered].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Between Real Air Quality Parameters", fontsize=14)
    plt.show()

def plot_all_graphs():
    """
    Executes all plotting functions to generate and save AQI, PM2.5 forecast, and correlation charts.
    """
    plot_aqi()
    plot_pm25_forecast()
    plot_correlation()


if __name__ == "__main__":
    plot_all_graphs()
