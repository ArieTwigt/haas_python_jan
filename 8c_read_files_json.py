#%% import library
from our_functions.import_functions import get_cars_by_brand
import json

#%%
with open("settings.json", "r") as file:
    settings_str = file.read()

#%%
settings = json.loads(settings_str)

# %%
settings
# %%
brand  = settings['brand']
export = settings['export'] 
type_file = settings['type_file']

#%%
get_cars_by_brand(brand, type_output=type_file, export_csv=export)
# %%
