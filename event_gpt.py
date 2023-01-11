import openai
import requests
from bs4 import BeautifulSoup
openai.api_key = "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"
scaleSerpKey = "54737D4576E3465B9A02285845AD6587"

#def get_sms(clean_links, shallowEvents):
def get_sms(clean_links):
    results = []
    prompt = "Name the type of food, drink, breakfast, lunch or dinner in the following event, as well as where and when it is. Use this format [event name, time, date, location, type of food/drink] "

    for link in clean_links:
    #scrape
        # set up the request parameters
        if "webapps.mines.edu" not in link:
            continue


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
        prompt += rawSoup

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
        results.append(event_string)
    """
    #adding the shallow search of the email to the deep search
    results.append(shallowEvents)
    #removing duplicates
    prompt = "Remove any duplicates from the following list and return the list again. Include a newline between each result. Keep eveything in this format [event name, time, date, location, type of food/drink]: " + "\n".join(results)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    sms = response['choices'][0]['text']
"""
    sms = "\n".join(results)
    return sms

