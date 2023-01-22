import requests
from bs4 import BeautifulSoup


def getTrain():
    URL = 'https://infopasazer.intercity.pl/?p=station&id=26211'

    page = requests.get(URL)


    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', attrs={'class':'table-delay'})
    table_body = table.find('tbody')

    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) #throw away empty values
    res = []
    for train in data:
        if (train[3][:3] == 'Poz'): # we are looking only for poznan - zbaszynek
            res.append(train)
    return res
    
def displayTrains():
    trains = getTrain()
    
    ans = ""
    if len(trains) == 0:
        ans = "Brak danych!"
    else:
        for row in trains:
            ans += ' '.join(row[:2]) + ' ' + ' '.join(row[2:]) + '\n'
        
    
    return ans