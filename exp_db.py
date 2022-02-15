#%%
import sqlite3

# %%
con = sqlite3.connect("database.db")

# %%
cursor = con.cursor()
# %%
qry_define_table = '''
CREATE TABLE training
(
    name text,
    participants real
)
'''

#%%
qry_insert_values =  '''
INSERT INTO training VALUES ('python', 10)
'''

#%%
cursor.execute(qry_define_table)

#%%
cursor.execute(qry_insert_values)
# %%
con.commit()
# %%
