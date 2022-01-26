## Assignments

#%% 1
full_name = "Arie Twigt"

# %% a.
full_name_new = full_name + " Jr."

print(full_name_new)
# %% b.
full_name_new = f"{full_name} Jr."
print(full_name_new)

# %% 2a specifiek
full_name_new = full_name_new.replace("Erling", "E.")
full_name_new

# %% b (generiek)
first_letter = full_name_new[0]
full_name_split = full_name_new.split(" ")
full_name_split[0] = first_letter + "."
full_name_abbrv = " ".join(full_name_split)
full_name_abbrv


#%% c
first_name = full_name_new.split(" ")[0]
full_name  = full_name_new.replace(first_name, f"{first_name[0]}.")
full_name

#%%
last_name = "Twigt"
full_name = first_name[0] + "." + last_name
full_name

# %% 3.
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)


# %% a. specifiek
combined_flower_list[1] = "daisy"
print(combined_flower_list)

#%% b. generiek
idx_tulip = combined_flower_list.index("tulip")
combined_flower_list[idx_tulip] = "daisy"

print(combined_flower_list)

# %% c. generiek als alle tulips vervangen moesten worden
# list comprehension
["daisy" if flower == "tulip" else flower for flower in combined_flower_list]


print(combined_flower_list_new)
# %%
