import requests
import json

def getAPOD():
    URL = 'https://api.nasa.gov/planetary/apod?api_key=c3Xnr5APjHEd6il0nJxf3tLL8ShSBdvUNgMISR9V'
    payload={}
    headers = {}

    response = requests.request("GET", URL, headers=headers, data=payload)

    dictionaryData = json.loads(response.text)
    # print(dictionaryData['title'])
    # print(dictionaryData['explanation'])
    # print(dictionaryData['hdurl'])
    result = [f"{dictionaryData['title']}\n{dictionaryData['explanation']}", dictionaryData['hdurl']]
    return result

