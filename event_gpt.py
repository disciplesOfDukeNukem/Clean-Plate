import openai
import requests
from bs4 import BeautifulSoup
openai.api_key = "INSERT_API_KEY"
scaleSerpKey = "INSERT_API_KEY"

#def get_sms(clean_links, shallowEvents):
def get_deep_events(clean_links):
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

    with open("rawEvents.txt", "a") as rE:
        for result in results:
            rE.write(result + "\n")


    

