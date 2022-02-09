#%%
groet_lambda = lambda x: print(f"Hallo {x}!")


#%%
def groet_fun(x):
    print(f"Hallo {x}!")

#%%
groet_lambda("Arie")
# %% inline if-statement
getal = 4

"Negatief" if getal < 0 else "Positief"


#%%
if getal < 0:
    "Negatief"
else:
    "Positief"


#%% 
check_negatief = lambda x: "Negatief" if x < 0 else "Positief"
# %%
check_negatief(5)
# %%
