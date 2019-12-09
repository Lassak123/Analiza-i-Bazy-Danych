#%%
import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
#%%
file = open('./../OrginalData/weather.txt')
data = file.read()
file.close()

data = re.sub('[BDS]?[\t ]+(OI|OS|SI|I+|S+)[\t ]*',',',data)
data = re.sub('[\t ]+',',',data)
data = re.sub('\s*,[\t ]*\n','\n',data)
data = re.sub('(\w+)(\d\d\d\d)(\d\d)(\w\w\w\w)','\g<1>,\g<2>,\g<3>,\g<4>',data)
data = data.replace('-9999','')

#Create headers
header = 'id,year,month,element'
for i in range(1,32):
    header += ',D'+str(i)
    
#Connect headers with data
data = header+'\n'+data

#Save *.txt file as *.csv 
file = open('./../AnalysisData/weather_raw.csv','w')
file.write(data)
file.close()
# %%
df = pd.read_csv('./../AnalysisData/weather_raw.csv')
df = pd.melt(df, id_vars=['id', 'year', 'month', 'element'],
             value_vars=list(df.columns)[4:],
             var_name='day', value_name='value')
df['day'] = df['day'].str[1:].astype('int')
df['day'] = df[['day']].apply(
    lambda row: '{:02d}'.format(*row),
    axis=1)
df = df.loc[df['value'] != '---', ['id', 'year', 'month','day', 'element', 'value']]
df = df.set_index(['id', 'year', 'month', 'day', 'element'])
df = df.unstack()
df.columns = list(df.columns.get_level_values('element'))
df = df.reset_index()
df.to_csv('./../AnalysisData/weather_tidy.csv', index=False)
#%% [markdown]
#Rozwiązanie zadania
#===================
#%% [markdown]
# Podczas zadania nalezało odpowiedzieć na pytania:`Która stacja zarejestrował największą różnicę temperatur w ciągu miesiąca? Określ które ze stacji zarejestrowały temperatury najbliższe do średniej wartości temperatury maksymalnej i minimalnej z poszczególnych miesięcy.`
#%% [markdown]
# Rozpocznijmy analizę danych

#%%
weather = pd.read_csv('./../AnalysisData/weather_tidy.csv')
weather.head()
#%%
weather.info()
#%%
weather.describe(include='all')
#%% [markdown]
#Odpowiedz
#==========

# %% [markdown]
# Zauważmy, że istnieje tylko jedno id, czyli jest tylko jedna stacja. Wynika z tego, że odpowiedziami na podane pytania jest ta jedna stacja.