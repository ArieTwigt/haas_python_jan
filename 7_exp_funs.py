#%%
from our_functions.calc_functions import calc_circle
from our_functions.greet_functions import greet_name

#%%
if __name__ == '__main__':
    diameter = input("Geef de diameter:\n") or 10
    print(calc_circle(diameter))