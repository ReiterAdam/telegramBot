import requests
import xmltodict

def getListOfDrivers():
    url = "http://ergast.com/api/f1/2022/drivers"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    my_dict = xmltodict.parse(response.text)
    listOfDrivers = my_dict['MRData']['DriverTable']['Driver']
    ans = "Here is list of drivers:\n"    
    for driver in listOfDrivers:
        ans += driver['PermanentNumber'] + ' ' + driver['GivenName'] + ' ' + driver['FamilyName'] + '\n'
    
    return ans
    
def getSchedules():

    url = "http://ergast.com/api/f1/{{year}}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)