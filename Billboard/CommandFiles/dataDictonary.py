import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
import plotly.express as px
#%% [markdown]
#DATA APPENDIX
#=============
#Author: Jakub Lassak
#
#In this database we have created two file.
#First one is `songData.csv`. It contains informations about informations abouts songs which we analize from `bilboard.csv`.
# The second one `rankingData.csv` contains informations about time when one song was in the list TOP 100.
#%% [markdown]
#songData
#=========
#%%
songs = pd.read_csv("./../AnalysisData/songData.csv")
songs.head()
#%%
songs.info()
#%%
songs.describe(include='all')
#%%
fig_genre = px.histogram(songs,x='genre')
fig_genre.show()
#%%
fig_artist = px.histogram(songs,x='artist.inverted')
fig_artist.show()

#%% [markdown]
#rankingData
#=========
#%%
ranking = pd.read_csv("./../AnalysisData/rankingData.csv")
ranking.head()
#%%
ranking.info()
#%%
ranking.describe(include='all')
#%%
fig_week = px.histogram(ranking,x='week')
fig_week.show()
fig_rank = px.histogram(ranking,x='rank')
fig_rank.show()