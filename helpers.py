import wolframalpha
import requests
import urllib.parse

# Configuring wolfram alpha app id
APP_ID = 'WLEY43-WJGR6QKPGU'
client = wolframalpha.Client(APP_ID)

def graph(query):
    answer = wolfram(query)

    return 0

def wolfram(query):
    # Contact API
    try: 
        url = f"http://api.wolframalpha.com/v2/query?appid={APP_ID}&input={urllib.parse.quote(query)}&output=json"
        print(url)
        response = requests.get(url).json()
    except:
        return "Error in Contacting API"
    # Give Back Answer
    try:
        answer = {}
        
        r=response["queryresult"]["pods"][0]["subpods"][0]
        answer["plaintext"] = r["plaintext"]
        answer["image"] = r["img"]["src"]
    except:
        return "Parsing Error"

    return answer
