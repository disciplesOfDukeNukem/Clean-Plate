#This file will parse the rawBlast and return the text

from bs4 import BeautifulSoup

#opening the rawBlast
with open("rawBlast.txt", 'r') as f:
    #saves it as raw_blast
    raw_blast = f.read()

#print(raw_blast)

soup = BeautifulSoup(raw_blast, 'html.parser')

text = soup.get_text()
print(text)