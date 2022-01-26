## Assignments

#%%

vowels = 'aeouiy' # definitie vowels
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter'] # definitie namen lijst

new_names_list = [] # lege namen lijst die wordt gevuld

for name in names_list:   # loop door de namen heen
    print(name)                                    # print the naam voor de zekerheid
    for letter in name:                                    # loop door iedere letter heen in de naam
        if letter.lower() in vowels:                      # als de letter, in de naam, voorkomt in 'vowels' ...
            name = name.replace(letter, "")               # verplaats die letter voor een lege character

                                # iedere keer wordt de 'name' overgeschreven
    new_names_list.append(name) # voeg de nieuwe naam toe aan de list

#%%
new_names_list
# %%
import locale

locale.setlocale(locale.LC_ALL, "nl_NL")


## Assignment 2
import datetime

current_date = datetime.date.today()

day_range = range(10)

for num_days in day_range:
    new_date = current_date + datetime.timedelta(days=num_days + 1)
    print(new_date.strftime("%A").capitalize())
# %%

#%% experimenteren met strftime
for num_days in day_range:
    new_date = current_date + datetime.timedelta(days=num_days + 1)
    print(new_date.strftime("A beautiful %A in the month of %B in the year %Y"))
# %%
