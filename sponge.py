import requests
import json

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