#%%
from fileinput import filename
import requests
from dotenv import load_dotenv
import os
import pandas as pd


import plotly
import plotly.express as px
import plotly.graph_objects as go




load_dotenv()

key = os.environ.get('WEATHER_KEY')

city = input("Give city:\n")

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
weather_wind        = []

for idx, value in enumerate(list_predictions):
    weather_temp.append(list_predictions[idx]['main']['temp'])                       # temperature

    weather_feels_like.append(list_predictions[idx]['main']['feels_like'])           # feels like temperature

    weather_wind.append(list_predictions[idx]['wind']['speed'])

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
                          "wind": wind,
                          "description": description}

                for temp, feels_like, wind, rain_mm, description, dt_txt
                in zip(weather_temp, weather_feels_like, weather_wind, weather_rain_mm, weather_description, weather_dt_txt)
            }


# create DataFrame from dictionary
weather_df = pd.DataFrame.from_dict(data=weather_dict, 
                                   orient='index')


weather_df = weather_df.reset_index()
weather_df.rename(columns={"index": "date_time"}, inplace=True)

weather_df['date_time'] = pd.to_datetime(weather_df['date_time'])

weather_df['date'] = weather_df['date_time'].dt.date
weather_df['week'] = weather_df['date_time'].dt.week
weather_df['year'] = weather_df['date_time'].dt.year


#%%


#%% compose plotly graph
fig = go.Figure()

#%%
fig.add_trace(go.Scatter(x=weather_df['date_time'], y=weather_df['temperature'],
                    mode='lines',
                    name='Temperature',
                    line=dict(color='royalblue', width=6))                 
                    )


fig.add_trace(go.Scatter(x=weather_df['date_time'], y=weather_df['feels_like'],
                    mode='lines',
                    name='Feels like',
                    line=dict(color='orange', width=3, dash='dot')))

fig.add_trace(go.Bar(x=weather_df['date'], y=weather_df['wind'],
                    name='Wind speed',
                    marker=dict(
                    color='gray',
                    line=dict(
                         color='gray',
                         width=1.5),
                       ),
                       opacity=0.6))


fig.add_trace(go.Bar(x=weather_df['date_time'], y=weather_df['rain_mm'], 
                     name='Rain (mm)',
                     marker=dict(
                     color='rgb(158,202,225)',
                     line=dict(
                         color='rgb(8,48,107)',
                         width=1.5),
                       ),
                       opacity=0.6))

                       
fig.update_layout(
    title="{} 3h weather forecast for 5 days".format(city),
    yaxis_title="Temperature (C)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)                                                             
# %% export visualisation
plotly.offline.plot(fig, 
                    filename = f"weather_export_{city}")

# %%
