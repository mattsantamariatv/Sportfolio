# Sportfolio

### bovada

1. run bovada_script.js - A json file gets created as the output
2. run bovada.lv_json_to_excel.py - A converted csv file gets created for the scraped data

### xbet

1. edit the file xbet_scrape
2. modify the line:fname = r"C:\Users\Kartik\Scraping_Project\results" + "\odds_xbet_" + str(today) + ".csv"
with the destination you wish to get your output in

### mlb elo

1. modify the line: urllib.request.urlretrieve('http://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv', "file.csv")
with the destination you wish to get your output in



##### possible errors in the python scripts:

"module not found" error: install the respective module in your computer

