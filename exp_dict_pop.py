#%%
persoon_dict = {}
persoon_dict['name'] = 'Arie'
persoon_dict['hobbies'] = ['Mountainbiken', 'Reading', 'Cooking']
# %%
persoon_dict['hobbies']
# %%
type(persoon_dict['hobbies'])
# %%
persoon_dict['hobbies'].remove('Reading')
# %%
persoon_dict['hobbies'].pop('Cooking')
# %%
persoon_dict.pop('name')
# %%
persoon_dict.pop('hobbies')
# %%
persoon_dict['hobbies'].pop(1)
# %%
persoon_dict
# %%
