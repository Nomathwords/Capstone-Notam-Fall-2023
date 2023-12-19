# A simple function that plots all of our calculated coordinates on a Google map.
# Green = Departure airport, Red = Destination airport, Blue = Flight path

import os
from gmplot import gmplot

def create_map(src_lat, src_long, dest_lat, dest_long, flight_coordinates):

    api_key = os.environ.get('google_maps_api_key')
    map_path = os.path.join( 'airport', 'map.html' )

    # Initialize the map at a given point
    gmap = gmplot.GoogleMapPlotter(39.0997, -94.5786, 4, apikey = api_key)

    # Add a marker for the departure airport
    gmap.marker(src_lat, src_long, 'green')

    # Add a marker for every pair of coordinates
    for coords in flight_coordinates:
        gmap.marker(flight_coordinates[coords][0], flight_coordinates[coords][1], 'cornflowerblue')

    # Add a marker for the destination airport
    gmap.marker(dest_lat, dest_long, 'red')

    # Draw map into HTML file
    gmap.draw(map_path)