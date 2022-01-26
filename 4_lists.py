#%%
flower_list = ['gerbera', 'lily', 'rose', 'tulip', 'tulip', 'gerbera']

#%%
unique_flowers = list(set(flower_list))
unique_flowers
# %%
name_list = ['Arie', 'Lily', 'Rose'] 
age_list  = [20, 30, 40]
# %%
dict(zip(name_list, age_list))
# %%
import requests



# %%
response = requests.get("https://opendata.rdw.nl/resource/m9d7-ebf2.json")
# %%
car_list = response.json()
# %%
import pandas as pd

cars_df = pd.DataFrame(car_list)
# %%
