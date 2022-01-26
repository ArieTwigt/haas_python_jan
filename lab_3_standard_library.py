## Assignments

#1
#%%
import datetime

#%% a. Specifiek
next_birthday = datetime.date(2022, 1, 28)
today_date    = datetime.date.today()
#%%

difference = (next_birthday - today_date).days
print(difference)

#%%
today_date - ten_days


#%%
datetime.date.today().isocalendar()

# %% b. Generiek
birthday_month = 1
birthday_day   = 28
current_year   = datetime.date.today().year
current_year_birthday = datetime.date(current_year, birthday_month, birthday_day)

#%%
current_date = datetime.date.today()
birthday_passed = current_date > current_year_birthday


if birthday_passed:
    next_year           = current_year + 1
    next_birthday       = datetime.date(next_year, birthday_month, birthday_day)
    days_until_birthday = next_birthday - current_date
    print(f"Days until next birthday: {days_until_birthday} days.")
else:
    next_birthday       = datetime.date(current_year, birthday_month, birthday_day)
    days_until_birthday = next_birthday - current_date
    print(f"Days until next birthday: {days_until_birthday} days.")


# 2.

#%%
import math

diameter = 10
radius = (diameter / 2)
surface_circle = math.pow(radius, 2) * math.pi
print(surface_circle)

# %%

# 3

#%%
import os

#%%
current_files = os.listdir()
current_files

#%% 4.
#%% a. Specifiek
os.mkdir("our_functions")


# %%
dir_name = "our_functions"

if dir_name not in current_files:
    os.mkdir(dir_name)
    print(f"Created {dir_name}")
else:
    print(f"Directory {dir_name} already exists.")
# %%
