#%%
from our_functions.import_functions import get_cars_by_brand


#%%
cars_df = get_cars_by_brand("TESLA", type_output="df")

# %%
def groet(type_groet, *args):
    for x in args:
        print(f"{type_groet} {x}!")

#%%
groet("Hallo!", "Arie", "Marco", "Mark", "Peter")
# %%
def beschrijf(beschrijving, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}, met als waarde: {value}")

#%%
beschrijf("Dit is", merk="Volvo", vermogen="100pk", prijs=10000)
# %%

'''
* args --> list
**kwargs --> dict
'''