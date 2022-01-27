#%%
import json

#%%
settings = {}
settings['brand']       = "BMW"
settings['export']      = True    

#%%
settings_str = json.dumps(settings)

#%%
with open("settings.json", "w") as file:
    file.write(settings_str)
# %%
