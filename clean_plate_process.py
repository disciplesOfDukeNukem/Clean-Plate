#Authors: Porter Frerickson and Zach Crennen

#test
#imports
import requests
import json
from bs4 import BeautifulSoup

#main which runs the whole program
def main():
    sponge()
    print("Clean Plate Bitches")


#scrapes the daily blast website to get the RawDawg html
def sponge():
    # set up the request parameters
    params = {
    'api_key': '54737D4576E3465B9A02285845AD6587',
    'q': 'pizza',
    'include_html': 'true',
    'output': 'html'
    }

    # make the http GET request to Scale SERP
    api_result = requests.get('https://webapps.mines.edu/DailyBlast/Home/PerformSearch', params)

    # print the HTML response from Scale SERP
    print(api_result.content)

    #outputting to an html file
    with open("rawBlast.txt", 'w') as rawBlast:
        rawBlast.write(api_result.content.decode('utf-8'))
    soap()


    #This file will parse the rawBlast and return the text
def soap():
        
    #opening the rawBlast
    with open("rawBlast.txt", 'r') as f:
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

main()
