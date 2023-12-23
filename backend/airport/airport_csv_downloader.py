import pandas as pd
import os

def download_airports_csv():

    # Path to the FAA Airports.csv file
    data = pd.read_csv('https://opendata.arcgis.com/api/v3/datasets/e747ab91a11045e8b3f8a3efd093d3b5_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1')

    # Path to the Airports.csv file
    airport_csv_path = os.path.join( 'airport', 'Airports.csv' )

    # Raw path of where you want to save the file (Remember to end it with 'name.csv'!) This puts it in the 'NOTAM\backend\airport' directory.
    data.to_csv(airport_csv_path)