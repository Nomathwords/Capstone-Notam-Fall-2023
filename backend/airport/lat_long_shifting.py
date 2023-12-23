import math
from . import mapper

def calculate_next_coordinate(src_lat, src_long, dest_lat, dest_long, step_size_in_nm):
    
    # 1 nautical mile = 1.150779448 miles
    conversion_factor = 1.150779448

    # Get distance in land miles
    land_dist = step_size_in_nm * conversion_factor

    # Calculate bearing
    bearing = calculate_bearing(src_lat, src_long, dest_lat, dest_long)

    # Calculate total distance
    total_dist = haversine_distance(src_lat, src_long, dest_lat, dest_long)
    
    # Calculate number of steps to reach destination
    steps = int(total_dist / land_dist)

    current_lat = src_lat
    current_long = src_long

    # Create a dictionary to store coordinates
    coordinates = {}

    # Calculate coordinates for each step
    for i in range(0,steps):
        # Calculate new coordinates
        new_lat, new_long = calculate_new_coordinates(current_lat, current_long, land_dist, bearing)
        # Add coordinates to dictionary
        coordinates[i + 1] = (new_lat, new_long)
        print(f'Step Coordinates: {new_lat} {new_long}')
        # Check if destination is reached
        if haversine_distance(new_lat, new_long, dest_lat, dest_long) <= land_dist:
            print("Reached Destination\n")
            break

        # Update current coordinates
        current_lat = new_lat
        current_long = new_long
        bearing = calculate_bearing(current_lat, current_long, dest_lat, dest_long)

    # Create map
    mapper.create_map(src_lat, src_long, dest_lat, dest_long, coordinates)

    return coordinates


def calculate_bearing(src_lat, src_long, dest_lat, dest_long):
    
    # Convert to radians
    src_lat = math.radians(src_lat)
    src_long = math.radians(src_long)
    dest_lat = math.radians(dest_lat)
    dest_long = math.radians(dest_long)

    # Difference in longitudes
    delta_long = dest_long - src_long

    # X and Y coordinates for bearing
    x = math.sin(delta_long) * math.cos(dest_lat)
    y = math.cos(src_lat) * math.sin(dest_lat) - (math.sin(src_lat) * math.cos(dest_lat) * math.cos(delta_long))

    # Calculate bearing
    bearing = math.atan2(x, y)
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360 # ??????

    return bearing


def calculate_new_coordinates(lat, long, distance, bearing):

    # Earth radius in miles
    earth_radius = 3960

    # Convert to radians
    lat, long, bearing = map(math.radians, [lat, long, bearing])
    distance = distance / earth_radius

    # Calculate new coordinates
    new_lat = math.asin(math.sin(lat) * math.cos(distance) + math.cos(lat) * math.sin(distance) * math.cos(bearing))
    new_long = long + math.atan2(math.sin(bearing) * math.sin(distance) * math.cos(lat), math.cos(distance) - math.sin(lat) * math.sin(new_lat))

    return math.degrees(new_lat), math.degrees(new_long)

def haversine_distance(src_lat, src_long, dest_lat, dest_long):

    # Convert to radians
    src_lat, src_long, dest_lat, dest_long = map(math.radians, [src_lat, src_long, dest_lat, dest_long])

    # Calculate difference in latitudes and longitudes
    dlat = dest_lat - src_lat
    dlon = dest_long - src_long

    # Calculate distance
    a = math.sin(dlat / 2) ** 2 + math.cos(src_lat) * math.cos(dest_lat) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return 3960 * c  # Earth radius in miles