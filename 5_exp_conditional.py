#%%
result = 5 > 4
# %%
if (5 > 4) and (1 == 2):
    print("Dit is true")
elif 3==4:
    print("De tweede keer")

# %%
print("We gaan verder")

#%%
gasten_lijst = ['Arie', 'Clark', 'Jim']
#%%

gast = 'Rose'

if gast not in gasten_lijst:
    print("U staat nog niet op de lijst")
    gasten_lijst.append(gast)
    print("Welkom")
else:
    print("U staat er al in")

# %%
name = 'Arie'

if 'A' in name:
    print("Bevat de letter 'A'")
# %%
