# get numbers from user
lat1 = float(input("Enter start latitude: "))
lon1 = float(input("Enter start longitude: "))
lat2 = float(input("Enter end latitude: "))
lon2 = float(input("Enter end longitude: "))

# check if values are valid
if lat1 < -90 or lat1 > 90 or lat2 < -90 or lat2 > 90:
    print("Invalid latitude! Must be between -90 and 90")

elif lon1 < -180 or lon1 > 180 or lon2 < -180 or lon2 > 180:
    print("Invalid longitude! Must be between -180 and 180")

else:
    # calculate distance
    distance = ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

    # print result
    print(f"Distance is: {distance:.4f}")