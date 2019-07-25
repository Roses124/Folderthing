'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
polarity = []
subjectivity = []
bad_words = ["they", "them", "you", "and", "also", "as", "well", "then", "make", "more", "that", "about", "than", "https", "by", "will", "it",  "my", "for", "the", "me", "a", "your", "we", "you", "us", "to", "too"]
#Get the JSON data
tweetFile = open("tweets_smallthing.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()



# Continue your program below!

bigtweet = ""


for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(text)
    polar = tb.polarity
    #polarstr =(polar)
    polarity.append(polar)
    subj = tb.subjectivity
    #sentsstr = (sents)

    subjectivity.append(subj)
    sumpol = sum(polarity)
    lenpol = len(polarity)
    averagepol = sumpol / lenpol
    sumsub = sum(subjectivity)
    lensub = len(subjectivity)
    averagesub = sumsub / lensub
    bigtweet += text
print("The average polarity is " + str(averagepol) + "!" )
print("The average subjectivity is " + str(averagesub) + "!")
bigblob = TextBlob(bigtweet)
filtered_words ={}
wordsList = bigblob.words

for words in wordsList:
    if not words.isalpha() or words in bad_words or len(words) <= 3 :
        continue
    else:
        filtered_words[words] = bigblob.word_counts[words]

        #tweet_string.join(t)
thingy = WordCloud().generate_from_frequencies(filtered_words)
plt.imshow(thingy, interpolation = 'bilinear')
plt.axis("off")
plt.show()
    #if text_str.isalpha():
    #    continue
    #elif text_str.isalpha() False and text_str in bad_words:


plt.hist(polarity, bins=[-1.0, -.75, -.5, -.25, 0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75])
plt.title('Polarity of Tweets')
plt.axis([-1, 1, 0, 100])
plt.plot([polarity])
plt.ylabel('Number of Tweets')
plt.xlabel('Polarity')
plt.grid(True)
plt.show()

plt.hist(subjectivity, bins=[0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75])
plt.title('Subjectivity of Tweets')
plt.axis([0, 1, 0, 100])
plt.plot([subjectivity])
plt.ylabel('Number of Tweets')
plt.xlabel('Subjectivity')
plt.grid(True)
plt.show()


plt.scatter(polarity, subjectivity)
plt.show()

# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)
