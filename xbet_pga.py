# PGA Futures

# -*- coding: utf-8 -*-
"""
XBet MLB Scrape
"""
# The requests module allows you to send HTTP requests using Python
# Beautiful Soup is a Python library for pulling data out of HTML and XML files
# pandas is a software library written for the Python programming language for data manipulation and analysis
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
# The OS module in python provides functions for interacting with the operating system

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os

#chdir() changes the current working directory to the given path

os.chdir(r"/Users/mattsantamaria/Desktop/Sportfolio" + "/mlb_daily_xbet_" + str(today) + ".csv")

#current local time

today = date.today()

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
        
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

url = 'https://xbet.ag/sportsbook/mlb/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

sp = soup.findAll(attrs={'data-wager-type': 'sp', 'data-league-id' : 5})
ml = soup.findAll(attrs={'data-wager-type': 'ml', 'data-league-id' : 5})
to = soup.findAll(attrs={'data-wager-type': 'to', 'data-league-id' : 5})

odds_sp = pd.DataFrame(columns = ["team", "sp", "gameid", "league"])

for i in range(0, len(sp)):
    x = sp[i]
    odds_sp = odds_sp.append({'team' : x.attrs['data-team'], 'sp' : x.attrs['data-odds'], 'gameid' : x.attrs['data-gameid'], 'league' : x.attrs['data-league-id']}, ignore_index = True)

odds_ml = pd.DataFrame(columns = ["team", "ml", "gameid", "league"])

for i in range(0, len(ml)):
    x = ml[i]
    odds_ml = odds_ml.append({'team' : x.attrs['data-team'], 'ml' : x.attrs['data-odds'], 'gameid' : x.attrs['data-gameid'], 'league' : x.attrs['data-league-id']}, ignore_index = True)

odds_to = pd.DataFrame(columns = ["team", "to", "gameid", "league"])

for i in range(0, len(to)):
    x = to[i]
    odds_to = odds_to.append({'team' : x.attrs['data-team'], 'to' : x.attrs['data-odds'], 'gameid' : x.attrs['data-gameid'], 'league' : x.attrs['data-league-id']}, ignore_index = True)

odds = odds_sp.merge(odds_ml, on = ['team', 'gameid', 'league'])
odds = odds.merge(odds_to, on = ['team', 'gameid', 'league'])

odds = odds.groupby(['gameid']).transform(lambda x: '|'.join(x))
odds = odds.drop_duplicates()

odds[['team1', 'team2']] = odds.team.str.split("|", expand = True)
odds[['sp1', 'sp2']] = odds.sp.str.split("|", expand = True)
odds[['ml1', 'ml2']] = odds.ml.str.split("|", expand = True)
odds[['to1', 'to2']] = odds.to.str.split("|", expand = True)

odds = odds.drop(['team', 'sp', 'ml', 'to', 'league'], axis = 1)

fname = r"/Users/mattsantamaria/Desktop/Sportfolio" + "/mlb_daily_xbet_" + str(today) + ".csv"

odds.to_csv(fname)
