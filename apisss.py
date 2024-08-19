import requests
import datetime

def calculateTime(milliseconds):
    seconds = milliseconds / 1000
    dateOfEarthquake = datetime.datetime.fromtimestamp(seconds)
    return dateOfEarthquake

def getData(startTime, endTime, latitude, longitude, maxradiuskm, minmagnitude):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

    response = requests.get(url, params={
        "format" : "geojson",
        "starttime" : startTime,
        "endtime": endTime,
        "latitude" : latitude,
        "longitude" : longitude,
        "maxradiuskm" : maxradiuskm,
        "minmagnitude": minmagnitude
    })
    data = response.json()

    for i in range(len(data['features'])):
        timeKey = data['features'][i]['properties']['time']
        print(f"{i}. Place: {data['features'][i]['properties']['place']}. Time: {calculateTime(timeKey)} Magnitude: {data['features'][i]['properties']['mag']}")

