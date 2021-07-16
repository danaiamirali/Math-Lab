import wolframalpha
import requests
import urllib.parse

# Configuring wolfram alpha app id
APP_ID = 'WLEY43-WJGR6QKPGU'
client = wolframalpha.Client(APP_ID)

def graph(query):
    answer = wolfram(query)

    return 0;

def wolfram(query):
    # Contact API
    url = f"http://api.wolframalpha.com/v2/query?input={urllib.parse.quote_plus(query.strip())}&appid={APP_ID}&output=json"
    print(url)
    response = requests.get(url)
    response.raise_for_status()
    # Give Back Answer

    print(response)

    return response
