# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:05:22 2019

@author: Kartik
"""

import json
import pandas as pd

with open('E:/puppeter/output/result.json') as json_file:  
    data = json.load(json_file)

odds = pd.DataFrame(columns = ['team1', 'team2', 'team1_runline', 'team2_runline', 'team1_win', 'team2_win', 'team1_total', 'team2_total'])
    
for i in range(0, len(data)):
    
    x = data[i]
    t1 = x['teamOne']
    t2 = x['teamTwo']
    
    team1 = t1['name']
    team1_runline = t1['runline']
    team1_win = t1['win']
    team1_total = t1['total']
    
    team2 = t2['name']
    team2_runline = t2['runline']
    team2_win = t2['win']
    team2_total = t2['total']
    
    odds = odds.append({'team1' : team1, 'team2' : team2, 'team1_runline' : team1_runline, 'team2_runline' : team2_runline, 'team1_win' : team1_win, 'team2_win' : team2_win, 'team1_total' : team1_total, 'team2_total' : team2_total}, ignore_index = True)    
    
odds.to_csv('odds_bovada.lv.csv')
