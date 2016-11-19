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
print(f.get_weathers())

# get observation forecast for today in Kalamazoo, MI
observation = owm.weather_at_place('Kalamazoo, US')
weather = observation.get_weather()

# temperature outside.
temperatures = weather.get_temperature('fahrenheit')
current_temperature = temperatures.get('temp')
stringTemperature = str(current_temperature)

# snow
snow = weather.get_snow()
print(snow)


# rain
rain = weather.get_rain()
print(rain)

new_status = 'Current temperature is ' + stringTemperature + ' degrees F.'

# tweet the current temperature
# status = api.PostUpdate(status = new_status)
# print(status.text)
