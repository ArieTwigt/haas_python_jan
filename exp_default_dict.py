#%%
from collections import defaultdict

#%%
persoon_dict = {}
persoon_dict['naam'] = 'Arie'
persoon_dict['leeftijd'] = '32'


#%%
persoon_dict['naam']
# %%
persoon_dict.keys()
# %%
persoon_dict['woonplaats']
# %%


persoon_dict = {}

#%%
collega_dict = defaultdict(lambda: 'Onbekend')


#%%
collega_dict['naam']  = 'Jim'
collega_dict['leeftijd'] = 25

#%%
collega_dict['woonplaats']
# %%
collega_dict.values()
# %%
