import twitter
import pyowm

# Twitter API keys for @MomBot13 user
api = twitter.Api(consumer_key='56cMPfOsNJY1fiNPXb8V22kzc',
                  consumer_secret='PNdmAqKjHP4Ph1duqEqwfnSVXp38qPYbUAxGQz3LrNoj1kZNxk',
                  access_token_key='796893994944970752-fkDDzlJnT7SpB4ntWPEqhrrzzCFQuXe',
                  access_token_secret='0FfQ0R6UWAMt2sYIiilX2W18h5tZ0u2QNFYGbFj2wf5cl')

# openweathermap.org API key
owm = pyowm.OWM('e8682fe7558aa979da504ee6e497460b')

# get observation forecast for today in Kalamazoo, MI
observation = owm.weather_at_place('Kalamazoo, US')
weather = observation.get_weather()
temperatures = weather.get_temperature('fahrenheit')
current_temperature = temperatures.get('temp')
stringTemperature = str(current_temperature)
x = 'Current temperature is', stringTemperature,'degrees F. Looks like no coat today.'

# tweet the current temperature
status = api.PostUpdate(x)
print(status.text)
