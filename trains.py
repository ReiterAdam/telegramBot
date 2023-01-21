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
    for pociag in data:
        if (pociag[3][:3] == 'Poz'): # we are looking only for poznan - zbaszynek
            res.append(pociag)
    return res