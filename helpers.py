import wolframalpha
import requests
import urllib.parse

# Configuring wolfram alpha app id
APP_ID = 'WLEY43-WJGR6QKPGU'

def wolfram(query, podscanner):
    # Contact API
    try:
        url = f"http://api.wolframalpha.com/v2/query?appid={APP_ID}&input={urllib.parse.quote(query)}&includepodscanner={podscanner}&output=json"
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
        print(answer)
    except:
        return "Invalid Input"

    return answer
