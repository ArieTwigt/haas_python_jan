## Assignments

#%% 1
name = "Arie"

if "a" in name.lower():
    print("Your name contains an A")
else:
    print("Your name does not contain an A")

# %% 2a
import random
import string

name = "Peter"

vowels = ['a', 'e', 'o', 'u', 'i']
letter_list = list(string.ascii_lowercase)

non_vowels = [letter 
              for letter in letter_list 
              if letter not in vowels]

if name[0].lower() in vowels:
    # random letter
    random_letter = random.choice(vowels)

    print("Your name begins with a vowel")
    name = name.replace(name[0], random_letter.upper())
    print(name)
else:
    # random letter
    random_letter = random.choice(non_vowels)

    print("Your name does not begin with a vowel")
    name = name.replace(name[0], random_letter.upper())
    print(name)


# %%
vowels = ['a', 'e', 'o', 'u', 'i']

random_vowel = random.choice(vowels)
random_vowel

#%%


# %%

# %%
