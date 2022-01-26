#%% 1
person = {}
person['name']    = "Clark"
person['age']     = 40
person['hobbies'] = ['football', 'tennis', 'mountainbike']


print(person)
#%% 2,
person_1 = {}
person_1['name']    = "Clark"
person_1['age']     = 40
person_1['hobbies'] = ['football', 'tennis', 'mountainbike']

person_2 = {}
person_2['name']    = "Louis"
person_2['age']     = 38
person_2['hobbies'] = ['running', 'reading']

person_3 = {}
person_3['name']    = "Jim"
person_3['age']     = 14
person_3['hobbies'] = ['pokemon', 'painting']

person_4 = {}
person_4['name']    = "Rose"
person_4['age']     = 16
person_4['hobbies'] = ['netflix', 'programming', 'traveling']


#%%

family = {}
family['name'] = "Kent"
family['members'] = [person_1, person_2, person_3, person_4]

# %% Bonus: Ophalen 2e hobby van persoon_4
family['members'][3]['hobbies'][1]

# %% Bonus: Toevoegen hobby aan "Jim"
family['members'][2]['hobbies'].append('gaming') 

# %%
family
# %%
family['city'] = 'Enschede'
# %%
family['members'][0]['age'] *= 3
# %%
family
# %%
family['members'][0]['name'] = "Harrie"
# %%
