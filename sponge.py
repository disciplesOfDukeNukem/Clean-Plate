import requests

def perform_search():
    # set up the request parameters
    params = {
    'api_key': '54737D4576E3465B9A02285845AD6587',
      'q': 'pizza',
      'include_html': 'true',
      'output': 'html'
    }

    # make the http GET request to Scale SERP
    api_result = requests.get('https://webapps.mines.edu/DailyBlast/Home/PerformSearch', params)
    return api_result.content

