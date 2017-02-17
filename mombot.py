#!/usr/bin/env python
import twitter
import pyowm
from auth import *

# Twitter API keys for @MomBot13 user
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

# openweathermap.org API key
owm = pyowm.OWM(weather_key)

fc = owm.three_hours_forecast('Kalamazoo, US')
f = fc.get_forecast()

# get observation forecast for today in Kalamazoo, MI
observation = owm.weather_at_place('Kalamazoo, US')
weather = observation.get_weather()

# temperature outside.
temperatures = weather.get_temperature('fahrenheit')
current_temperature = temperatures.get('temp')
stringTemperature = str(current_temperature) + 'F'

status = weather.get_status()

if (status == 'Rain'):
    precipitation = 'Rainy... grab an umbrella too. '
elif (status == 'Snow'):
    precipitation = 'May the hat and gloves be with you.'
else:
    precipitation = ''

if (current_temperature > 70):
    new_status = 'Hot and sweaty at ' + stringTemperature + '. ' + precipitation
elif (70 >= current_temperature >= 60):
    new_status = 'Enjoy the perfect weather at - ' + stringTemperature + precipitation
elif (20 <= current_temperature < 45):
    new_status = 'May the coat, hat and gloves be with you. ' + precipitation + stringTemperature
else:
    new_status = 'It is better to stay inside and drink hot baverages. Temperature is at ' + stringTemperature

# tweet the current temperature
status = api.PostUpdate(status = new_status)
print(status.text)
