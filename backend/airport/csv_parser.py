import csv, sys

#path to airport csv file
airport_csv_path = ''

# define Python user-defined exceptions
class InvalidFilePathException(Exception):
    "Error!! The file path to the Airports.csv file is invalid!"
    pass

def get_lat_long(departure, destination):
    #variables to hold lat and long values for dep and dest
    dep_lat = -1.0
    dep_long = -1.0
    dest_lat = -1.0
    dest_long = -1.0
    
    try: 
        #Parse the csv file 
        with open(airport_csv_path, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #if the airport names are found in the csv file 
                if row['IDENT'] == departure:
                    print(row.keys())
                    dep_lat = row['Y']
                    dep_long = row['X']
                elif row['IDENT'] == destination:
                    dest_lat = row['Y']
                    dest_long = row['X']
    except FileNotFoundError:
        print("Oops! Airport.csv file is not found in the given path")
        sys.exit(1)


    #print out the values and return the coordinates 
    print(departure, ": ", dep_lat, dep_long)
    print(destination, ": ", dest_lat, dest_long)
    return float(dep_lat), float(dep_long), float(dest_lat), float(dest_long)
         