import requests
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()

key = os.environ.get('WEATHER_KEY')

city = "Utrecht"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=metric"

response  = requests.get(url)
resp_dict = response.json()

list_predictions = resp_dict['list']

# loop through all predictions
weather_temp        = []
weather_feels_like  = []
weather_rain_mm     = []
weather_description = []
weather_dt_txt      = []

for idx, value in enumerate(list_predictions):
    weather_temp.append(list_predictions[idx]['main']['temp'])                       # temperature

    weather_feels_like.append(list_predictions[idx]['main']['feels_like'])           # feels like temperature

    try:
        weather_rain_mm.append(list_predictions[idx]['rain']['3h'])
    except KeyError:                                                                          # rain
        weather_rain_mm.append(0.0)

    weather_description.append(list_predictions[idx]['weather'][0]['description'])   # description

    weather_dt_txt.append(list_predictions[idx]['dt_txt'])                           # date_txt


# compose dictionary with dict comprehension
weather_dict = {dt_txt : {"temperature": temp, 
                          "feels_like": feels_like,
                          "rain_mm": rain_mm,
                          "description": description}

                for temp, feels_like, rain_mm, description, dt_txt
                in zip(weather_temp, weather_feels_like, weather_rain_mm, weather_description, weather_dt_txt)
            }


# create DataFrame from dictionary
weather_df = pd.DataFrame.from_dict(data=weather_dict, orient='index')

pass




