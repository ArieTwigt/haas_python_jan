#%%
namen_lijst   = ['Arie', 'Jan', 'Dirk']
namen_lijst_2 = ['Piet', 'Mark', 'Roos']

#%%
for naam in namen_lijst:
    print(f"Hallo {naam}!")

# %% defineer de functie/generator
def namen_gen(name_list):
    num = 0
    while num < len(name_list):
        yield(f"Hallo {name_list[num]}!")
        num +=1




#%% maak een generator aan
give_names  =  namen_gen(namen_lijst)
give_names_2 =  namen_gen(namen_lijst_2)











#%%
def 



#%%
next(give_names)



#%%
next(give_names_2)


# %%
next(give_names)
# %%
print("Code")


#%%
print("Nog meer code")


#%%
next(give_names)

#%%
print("Meer code")


#%% 
next(give_names)