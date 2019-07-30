import billionaires
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
#from wordcloud import WordCloud
list_of_richies = billionaires.get_billionaires()

locationstring = ""
countlocal= {}
usedlist = []
percentcountry = {}
all_countries = []

for row in list_of_richies:
    onelist =row["location"]["country code"]
    locationstring += onelist + ","

lb = TextBlob(locationstring)
locationlist = lb.words
for code in locationlist:
    if code in usedlist:
        countlocal[code] += 1
    else:
        countlocal[code] = 1
        usedlist.append(code)
#print(countlocal)

total = len(locationlist)

for location in locationlist:
    if location in all_countries:
        continue
    else:
        all_countries.append(location)

#print(all_countries)

for country in all_countries:
    b4percent = countlocal[country] / total
    afterpercent = b4percent * 100
    afterpercent2 = str(int(afterpercent)) + "%"
    percentcountry[country] = afterpercent2

print(percentcountry)
