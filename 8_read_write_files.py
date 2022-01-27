#%%
file = open("my_text.txt", "w")
file.write("Dit komt van python")
file.close()

# %%
with open("my_text_2.txt", "a") as file:
    file.write("Dit komt van python")

# %%
with open("my_text_2.txt", "r") as file:
    content = file.read()
# %%
