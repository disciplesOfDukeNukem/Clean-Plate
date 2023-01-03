#will make an API call for each event, and add it a finalSMS.txt
    #input: cleanLinks.csv
    #output: finalSMS.txt

import openai
import requests
from bs4 import BeautifulSoup
openai.api_key = "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"
scaleSerpKey = "54737D4576E3465B9A02285845AD6587"

links = []
prompt = "Name the type of food, drink, breakfast, lunch or dinner in the following event, as well as where and when it is. Use this format [event name, time, location, type of food/drink] "

readpath = "sampleCleanLinks.csv"

with open(readpath, "r") as cl:
    for line in cl:
        links.append(line.strip())

for link in links:
#scrape
    # set up the request parameters
    params = {
        'api_key': scaleSerpKey,
        'q': 'pizza',
        'include_html': 'true',
        'output': 'html'
        }

    # make the http GET request to Scale SERP
    api_result = requests.get(link, params)
    #print(api_result.content)

#parse
    soup = BeautifulSoup(api_result.content, 'html.parser')
    rawSoup = soup.get_text()
    ingredients = rawSoup.split('Campus Announcements')
    cookedSoup = ingredients[1]
    print(cookedSoup)
    prompt += cookedSoup

#prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    event_string = response['choices'][0]['text']
    print(event_string)

