import billionairesproject
import billionaires
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = 'USA', 'DEU', 'CHN', 'RUS', 'JPN', 'BRA', 'HKG', 'FRA', 'CAN', 'ITA', 'IND', 'GBR', 'MEX', 'CHE', 'ESP', 'TAIWAN', 'IDN', 'KOR', 'MYS', 'AUS', 'TUR', 'Other'
sizes = [34, 6, 5, 4, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 27]
colors = ['blue', 'green', 'red', 'darkred', 'lightcoral', 'darkgreen', 'yellow', 'brown', 'orange', 'purple', 'lightskyblue', 'darkblue', 'blue', 'green', 'red', 'darkred', 'lightcoral', 'darkgreen', 'yellow', 'brown', 'orange', 'purple', 'gray']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode, labels, colors)
#autopct='%1.1f%%', shadow=True, startangle=140

plt.axis('equal')
plt.show()
