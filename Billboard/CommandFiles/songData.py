import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("./../OriginalData/billboard.csv")

#Get only intresting information
df1 = df[['artist.inverted','track', 'time','genre']]

for index, row in df1.iterrows():
    time = re.findall('\d+',row['time'])
    time_sec = int(time[0])*30+int(time[1])
    row['time']=time_sec
#Sort data
df1 = df1.sort_values(ascending=True, by=["artist.inverted","track","time","genre"])

#Reset index
df1.reset_index(inplace =True, drop=True)
df1.index.name='id'

#Save to file
df1.to_csv("./../AnalysisData/songData.csv")
