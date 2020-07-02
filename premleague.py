#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt


# In[23]:


prem = pd.read_csv('Downloads/season-1819_csv.csv')
home_column = prem['HomeTeam']
home_teams = home_column.unique()

fig, ax = plt.subplots()

for team in home_teams:
    team_df = prem[prem['HomeTeam'] == team]
    
    plt.bar(team, (team_df['FTR'].count('H'))
    
ax.set_xlabel('Win')
ax.set_xticklabels(sports, rotation=90)

plt.show()


# In[ ]:





# In[ ]:




