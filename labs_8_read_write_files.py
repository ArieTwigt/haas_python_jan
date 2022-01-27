#%% 1



#%%
with open("my_story.txt", "w") as file:
    file.write("Once there was a Pyton developer\n")

with open("my_story.txt", "a") as file:
    file.write("He got a lot of IndentationErrors\n")

with open("my_story.txt", "a") as file:
    file.write("The End")

#%% 2
with open("my_story.txt", "r") as file:
    story_list = file.readlines()

# %% 3
story_upper = " ".join(story_list).upper()


#%%
with open("my_story_open.txt", "w") as file:
    file.write(story_upper)


# %% 4
import os

current_files_dirs = os.listdir()

dir_name = "stories"

if dir_name not in current_files_dirs:
    print(f"Creating folder {dir_name}")
    os.mkdir(dir_name)

#%%
with open(f"{dir_name}/my_story_upper_2.txt", "w") as file:
    file.write(story_upper)


# %%
