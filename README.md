<h1>Изучаю API. Проект 1</h1>

<h2>Консольное приложение для просмотра информации о землетрясениях</h2>
Данное приложение использует API с сайта

https://www.usgs.gov/programs/earthquake-hazards

с параметрами запроса можно ознакомиться здесь: https://earthquake.usgs.gov/fdsnws/event/1/

В файле `earthquake_app.py` содержится ввод данных от пользователя и вызов функции `getData` из файла `apisss.py`.<br>
В файле `apisss.py` содержится основная логика запроса:

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
<br>
  `response = requests.get` отправляет запрос по указанному `url` с параметрами `params={<br>
        "format" : "geojson",
        "starttime" : startTime,
        "endtime": endTime,
        "latitude" : latitude,
        "longitude" : longitude,
        "maxradiuskm" : maxradiuskm,
        "minmagnitude": minmagnitude
    })`, где
    <br>
`startTime` — время начала поиска землетрясений (в формате UTC);<br>
`endTime` — время окончания поиска землетрясений (в формате UTC);<br>
`latitude` — широта области поиска;<br>
`longitude` — долгота области поиска;<br>
`maxradiuskm` — максимальный радиус поиска в километрах;<br>
`minmagnitude` — минимальная магнитуда землетрясений для отображения.<br>
    
  data = response.json()`

