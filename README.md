# Sportfolio

### bovada

1. edit bovada_script.js - it's a javascript file
2. take the line - fs.writeFile("output/result.json", jsonContent, 'utf8', function (err) and replace the destination with wherever you want the output to be written
3. once you have set the output run the file and a json file gets created as the output
4. now edit the file bovada.lv_json_to_excel.py which is a python file
5. modify the line: with open('E:/puppeter/output/result.json') as json_file
with the location of the json file you just created
6. modify the  line: odds.to_csv('odds_bovada.lv.csv')
with the destination of the converted excel file or where you want the output of the scraped data

### xbet

1. edit the file xbet_scrape
2. modify the line:fname = r"C:\Users\Kartik\Scraping_Project\results" + "\odds_xbet_" + str(today) + ".csv"
with the destination you wish to get your output in

###
###

### mlb elo

1. modify the line: urllib.request.urlretrieve('http://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv', "file.csv")
with the destination you wish to get your output in

##### possible errors in the python scripts:

"module not found" error: install the respective module in your computer

