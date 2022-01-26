#%%
namen_lijst = ['arie', 'jim', 'rose', 'gerard', 'ietje']


#%%
for idx, name in enumerate(namen_lijst):
    print(idx)
    print(name)

# %%
leeftijden_lijst = [10, 20, 30, 40 , 50]

personen_dict = dict(zip(namen_lijst, leeftijden_lijst))
# %%
personen_dict
# %%
for value in personen_dict.items():
    print(value)

# %%
'''
break
continue
pass
'''

#%%
zoek_naam = 'rose'

namen_lijst = ['arie', 'jim', 'rose', 'gerard', 'ietje']

for naam in namen_lijst:
    print(naam)
    
    if naam == zoek_naam:
        pass

    nieuwe_naam = naam.upper()
    print(f"{nieuwe_naam}!")

print("De code wordt vervolgd")


# %%
class Car:
    pass
# %%
namen_lijst = ['arie', 'jim', 'rose', 'gerard', 'ietje']

upper_namen_lijst = []

for naam in namen_lijst:
    print(naam)
    upper_namen_lijst.append(naam.upper())    

#%%
upper_namen_lijst = [naam.upper() for naam in namen_lijst if naam[0] != "a"]
upper_namen_lijst
# %%
getallen_lijst = [5, 10, 19, 4, 21, 5]
[getal * 2 for getal in getallen_lijst]
# %%
