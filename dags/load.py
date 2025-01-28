import pandas as pd
import sqlite3

def load_data(**kwargs):
    """
    Loads cleaned air quality data into an SQLite database.

    This function reads a cleaned CSV file containing air quality data,
    then stores it in an SQLite database.

    Args:
        **kwargs: Arbitrary keyword arguments (not used explicitly in this function).

    Process:
        - Reads the cleaned dataset from `/tmp/cleaned_air_quality.csv`.
        - Connects to (or creates) an SQLite database `air_quality.db`.
        - Stores the data in a table named `air_quality`.
        - If the table already exists, it is replaced with the new data.
        - Closes the database connection.

    Output:
        - An SQLite database file `air_quality.db` containing the air quality data.

    Notes:
        - The database file is stored in the current working directory.
        - The table is **replaced** on every execution, meaning old data is overwritten.
        - Ensure that the file `/tmp/cleaned_air_quality.csv` exists before running this function.
    """

    DB_PATH = '/Users/tetiana/test_db/air_quality.db'
    df = pd.read_csv('/tmp/cleaned_air_quality.csv')

    conn = sqlite3.connect(DB_PATH)
    df.to_sql('air_quality', conn, if_exists='replace', index=False)
    conn.close()

