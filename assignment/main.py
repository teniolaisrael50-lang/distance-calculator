import math
 
#_latitude
def valid_latitude(lat):
    return -90 <= lat <= 90
#_longitude
def valid_longitude(lon):
    return -180 <= lon <= 180

while True:
    lat1 = float(input("Enter start latitude: "))

    if valid_latitude(lat1):
        break
    else:
        print("Invalid latitude! Must be between -90 and 90")

while True:
    lon1 = float(input("Enter start longitude: "))

    if valid_longitude(lon1):
        break
    else:
        print("Invalid longitude! Must be between -180 and 180")

while True:
    lat2 = float(input("Enter end latitude: "))

    if valid_latitude(lat2):
        break
    else:
        print("Invalid latitude! Must be between -90 and 90")

while True:
    lon2 = float(input("Enter end longitude: "))

    if valid_longitude(lon2):
        break
    else:
        print("Invalid longitude! Must be between -180 and 180")


# Distance formula
distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)


print(f"Distance: {distance} km")
