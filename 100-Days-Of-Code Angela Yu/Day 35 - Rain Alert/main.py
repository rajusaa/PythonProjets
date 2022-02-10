# Alert if weather forecasts indicates rain in the next 12 hours for a give Lat & Long value


import requests
API_KEY = 'XXXXXXXXXXXXXXXX' #API KEY should be updated
URL = 'https://api.openweathermap.org/data/2.5/onecall'
EXCLUDE = 'daily,minutely'

parameters = {
    'lat':33.44,
    'lon':-94.04,
    'exclude':EXCLUDE,
    'appid':API_KEY
}

response = requests.get(URL,params=parameters)
response.raise_for_status()
#print(response.json())
weather_data = response.json()
hourly_weather_data = weather_data['hourly'][:12]
print(hourly_weather_data[0]['weather'][0]['id'])
alert = False

for data in hourly_weather_data:
    print (data['weather'][0]['id'])
    if data['weather'][0]['id'] < 700 :
        alert = True

if alert:
    print('Bring Umbrella')