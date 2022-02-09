#%%
import requests
import pandas as pd

#%%
endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
resp = requests.get(endpoint)

#%%
cars_df = pd.DataFrame(resp.json())


# %%
