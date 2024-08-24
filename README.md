<h1>Изучаю API. Проект 1</h1>

<h2>Консольное приложение для просмотра информации о землетрясениях</h2>
Данное приложение использует API с сайта

https://www.usgs.gov/programs/earthquake-hazards

с параметрами запроса можно ознакомиться здесь: https://earthquake.usgs.gov/fdsnws/event/1/

В файле `earthquake_app.py` содержится ввод данных от пользователя и вызов функции `getData` из файла `apisss.py`.<br>
В файле `apisss.py` содержится основная логика запроса:

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?" 
<br>
  `response = requests.get` отправляет запрос по указанному `url` с параметрами 
  
    params={
          "format" : "geojson",
          "starttime" : startTime,
          "endtime": endTime,
          "latitude" : latitude,
          "longitude" : longitude,
          "maxradiuskm" : maxradiuskm,
          "minmagnitude": minmagnitude
      })
    
, где
    <br>
`startTime` — время начала поиска землетрясений (в формате UTC, например "2004-01-01");<br>
`endTime` — время окончания поиска землетрясений (в формате UTC, например "2014-01-01");<br>
`latitude` — широта области поиска(например "55.75");<br>
`longitude` — долгота области поиска(например "37.61");<br>
`maxradiuskm` — максимальный радиус поиска в километрах(например "150");<br>
`minmagnitude` — минимальная магнитуда землетрясений для отображения.(например "3.7")<br>
Такие параметры найдут все землетрясения магнитудой выше 3.7 в радиусе 150 км от точки с координатами 55.75, 37.61 (Москва) с 01.01.2004 по 01.01.2014, то есть за 10 лет. <br>
`data = response.json()` формирует данные из ответа в формате JSON.

Достаем нужные данныые из ответа:


        for i in range(len(data['features'])):

                timeKey = data['features'][i]['properties']['time']
        
                print(f"{i}. Place: {data['features'][i]['properties']['place']}. Time: {calculateTime(timeKey)} Magnitude: {data['features'][i]['properties']['mag']}")


