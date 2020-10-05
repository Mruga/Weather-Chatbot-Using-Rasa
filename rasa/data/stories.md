## story 1
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
  
## story 2
* goodbye
	- utter_goodbye

## story 3
* ask_weather
	- utter_ask_location

## story 4
* ask_weather_location
	- action_weather

## story 5
* ask_temperature
	- action_temp

* affirm
    - utter_affirm_response

## Generated Story 1
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather_location{"location": "stuttgart"}
    - slot{"location": "stuttgart"}
    - action_weather
    - slot{"location": "stuttgart"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 2
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
    - slot{"location": "berlin"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 3
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_temperature{"location": "Oslo"}
    - slot{"location": "Oslo"}
    - action_temp
    - slot{"location": "Oslo"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 4
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "cologne"}
    - slot{"location": "cologne"}
    - action_weather
    - slot{"location": "cologne"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 5
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "Kiel"}
    - slot{"location": "Kiel"}
    - action_weather
    - slot{"location": "Kiel"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 6
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather_location{"location": "Jamaica"}
    - slot{"location": "Jamaica"}
    - action_weather
    - slot{"location": "Jamaica"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 7
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "dhaka"}
    - slot{"location": "dhaka"}
    - action_weather
    - slot{"location": "dhaka"}
    - utter_did_that_help
* ask_weather_location{"location": "Chittagang"}
    - slot{"location": "Chittagang"}
    - action_weather
    - slot{"location": "Chittagang"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 8
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_temperature{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - action_temp
    - slot{"location": "Frankfurt"}
    - utter_did_that_help
* ask_temperature{"location": "Bonn"}
    - slot{"location": "Bonn"}
    - action_temp
    - slot{"location": "Bonn"}
    - utter_did_that_help
* affirm
    - utter_affirm_response
* affirm
    - utter_affirm_response
* thank
    - utter_thanks_response
* goodbye
    - utter_goodbye

## Generated Story 9
* greet
  - utter_ask_howcanhelp
* random_text
  - utter_end
* greet_query
  - utter_query_response
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "hongkong"}
    - slot{"location": "hongkong"}
    - action_weather
    - utter_did_that_help
    
## Story thanks response
* thank
    - utter_thanks_response