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

# get observation forecast for today in Kalamazoo, MI
observation = owm.weather_at_place('Kalamazoo, US')
weather = observation.get_weather()
temperatures = weather.get_temperature('fahrenheit')
current_temperature = temperatures.get('temp')
stringTemperature = str(current_temperature)
new_status = 'Current temperature is ' + stringTemperature + ' degrees F.'

# tweet the current temperature
status = api.PostUpdate(status = new_status)
print(status.text)
