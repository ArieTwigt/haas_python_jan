import requests
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ.get('WEATHER_KEY')

city = "Utrecht"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"

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

    weather_rain_mm.append(list_predictions[idx]['rain']['3h'])                      # rain

    weather_description.append(list_predictions[idx]['weather'][0]['description'])   # description

    weather_dt_txt.append(list_predictions[idx]['dt_txt'])                           # date_txt