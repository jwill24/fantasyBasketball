import requests
import pandas as pd
import os
import csv

url = 'https://hashtagbasketball.com/fantasy-basketball-rankings'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
#print df
df.to_csv('draftData.csv')

exists = os.path.isfile('picks.csv')
if exists: os.remove('picks.csv')

with open('picks.csv', 'a') as csvfile:
    writer=csv.writer(csvfile, delimiter=",")
    writer.writerow(['NAME','FG','FT','TRES','PTS','REB','AST','STL','BLK','TO'])
