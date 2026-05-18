# Import math 
import math

# Function to check if latitude is valid
def valid_latitude(latitude):
    return -90 <= latitude <= 90

# Function to check if longitude is valid
def valid_longitude(longitude):
    return -180 <= longitude <= 180

# Function to collect valid latitude from user
def get_latitude(message):
    while True:
        try:
            latitude = float(input(message))

           
            if valid_latitude(latitude):
                return latitude
            else:
                print("Invalid latitude! Must be between -90 and 90")

        # Handle error if user enters text instead of number
        except ValueError:
            print("Please enter a valid number")

# Function to collect valid longitude from user
def get_longitude(message):
    while True:
        try:
            longitude = float(input(message))

            # Check if longitude is within valid range
            if valid_longitude(longitude):
                return longitude
            else:
                print("Invalid longitude! Must be between -180 and 180")

        # Handle error if user enters text instead of number
        except ValueError:
            print("Please enter a valid number")

# Collect user inputs
lat1 = get_latitude("Enter start latitude: ")
lon1 = get_longitude("Enter start longitude: ")
lat2 = get_latitude("Enter end latitude: ")
lon2 = get_longitude("Enter end longitude: ")

# Convert latitude and longitude from degrees to radians
lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

#  calculations
dlat = lat2 - lat1
dlon = lon2 - lon1

a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Radius of Earth in kilometers
radius = 6371

# Calculate distance
distance = radius * c

# Display result
print(f"The distance is {distance:.2f} km")
