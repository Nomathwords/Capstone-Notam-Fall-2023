import csv, sys
import os

#path to airport csv file
airport_csv_path = os.path.join( 'airport', 'Airports.csv' )

def get_lat_long(departure, destination):
    #variables to hold lat and long values for dep and dest
    dep_lat = -1.0
    dep_long = -1.0
    dest_lat = -1.0
    dest_long = -1.0
    
    try: 
        # Parse the csv file 
        with open(airport_csv_path, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # If the airport names are found in the csv file 
                if row['IDENT'] == departure:
                    dep_lat = row['Y']
                    dep_long = row['X']
                elif row['IDENT'] == destination:
                    dest_lat = row['Y']
                    dest_long = row['X']

    # Handle errors as necessary
    except FileNotFoundError as file_err:
        print( "Airport.csv file could not be found. Does it exist?" )
        raise file_err
    except Exception as err:
        print( f"An unexpected exception occured. Details: {err}" )
        raise err

    # Print out the values and return the coordinates 
    print(f'{departure}: {dep_lat} {dep_long}')
    print(f'{destination}: {dest_lat} {dest_long}\n')
    return float(dep_lat), float(dep_long), float(dest_lat), float(dest_long)
         