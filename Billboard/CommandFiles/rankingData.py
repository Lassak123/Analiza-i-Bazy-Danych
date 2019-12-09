import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("./../OriginalData/billboard.csv")

# Melting
id_vars = ["year",
           "artist.inverted",
           "track",
           "time",
           "genre",
           "date.entered",
           "date.peaked"]

df = pd.melt(frame=df,id_vars=id_vars, var_name="week", value_name="rank")

# Formatting 
df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)
df["rank"] = df["rank"].astype('int32',errors = 'ignore')

# Cleaning out unnecessary rows
df = df.dropna()

# Create "date" columns
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)

df = df[["year", 
         "artist.inverted",
         "track",
         "time",
         "genre",
         "week",
         "rank",
         "date"]]
df = df.sort_values(ascending=True, by=["year","artist.inverted","track","week","rank"])
df.reset_index(inplace =True, drop=True)

sd = pd.read_csv("./../AnalysisData/songData.csv")

#Assigning new indexes
new_id = [None]*(len(df.index))
n=0
for i in range(len(df.index)):
    ser = df.loc[i,'track']
    if(ser == sd.loc[n,'track']):
        new_id[i]=n
    else:
        n= n +1
        new_id[i]=n
    #print(i)
df['id'] = new_id
df.set_index('id', inplace=True)

#Take only interesting data
df = df[['week', 'rank' ,'date']]

#Save to file
df.to_csv("./../AnalysisData/rankingData.csv")
    




    
