#from rasa_core.actions import Action
#from rasa_core.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import time
import requests

'''Get "action_weather" data'''


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        app_id = "JnnC8L7yA6ebC44rCiuj"
        app_key = "twQ8s3NiYo2MCBZfj1pZAQ"
        base_url = "https://weather.api.here.com/weather/1.0/report.json?"

        location = tracker.get_slot('location')
        print("In Action Weather",location)
        Final_url = base_url + "app_id=" + app_id + "&app_code=" + app_key + "&product=observation&name=" + location
        print("Final URL", Final_url)
        weather_data = requests.get(Final_url).json()


        if (len(weather_data) > 2):
            # JSON data works just similar to python dictionary and you can access the value using [].
            current_temperature = weather_data['observations']['location'][0]['observation'][0]['temperature']
            wind = weather_data['observations']['location'][0]['observation'][0]['windSpeed']
            desc = weather_data['observations']['location'][0]['observation'][0]['description']

            response = """ It is {} in {} at this moment. The temperature is {} degree and the wind speed is {} m/s. """.format(
                desc, location, current_temperature, wind)
            dispatcher.utter_message(response)
        else:
            dispatcher.utter_message("City Not Found ")


'''Get "action_temp" data'''


class ActionTemperature(Action):
    def name(self):
        return 'action_temp'

    def run(self, dispatcher, tracker, domain):
        app_id = "JnnC8L7yA6ebC44rCiuj"
        app_key = "twQ8s3NiYo2MCBZfj1pZAQ"
        base_url = "https://weather.api.here.com/weather/1.0/report.json?"

        location = tracker.get_slot('location')
        print("In Action Temperature", location)
        Final_url = base_url + "app_id=" + app_id + "&app_code=" + app_key + "&product=observation&name=" + location
        print("Final URL", Final_url)
        weather_data = requests.get(Final_url).json()

        if (len(weather_data) > 2):
            # JSON data works just similar to python dictionary and you can access the value using [].
            current_temperature = weather_data['observations']['location'][0]['observation'][0]['temperature']

            response = """ The temperature in {} is now {} degree currently """.format(location, current_temperature)
            dispatcher.utter_message(response)
        else:
            dispatcher.utter_message("City Not Found ")
