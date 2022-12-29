#This file will parse the rawBlast and return the text

from bs4 import BeautifulSoup

#will be rawBlast, using sample for testing purposes
openpath = "sampleDailyBlast-11-30-22.txt"

#opening the rawBlast
with open(openpath, 'r') as f:
    #saves it as raw_blast
    raw_blast = f.read()

#print(raw_blast)

soup = BeautifulSoup(raw_blast, 'html.parser')
rawSoup = soup.get_text()
ingredients = rawSoup.split('Maximum number of entries to return. If blank, no limit on number:\n\n\n\n\n\n')
cookedSoup = ingredients[1]
# Split the text into a list of words
words = cookedSoup.split()
# Get the first 2000 words
halfSoup = words[:2000]
# Join the first 2000 words back into a single string
cookedSoup = ' '.join(halfSoup)

print(cookedSoup)

with open("cleanBlast.txt", 'w') as rawBlast:
    rawBlast.write(cookedSoup)