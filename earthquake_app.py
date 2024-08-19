from apisss import getData


startTime = input("Enter the start time ")
endTime = input("Enter the end time ")
latitude = input("Enter the latitude ")
longitude = input("Enter the longitude ")
maxRadiusInKm = input("Enter the max radius in km ")
minMagnitude = input("Enter the min magnitude ")


getData(startTime, endTime, latitude, longitude, maxRadiusInKm, minMagnitude)