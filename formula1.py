import requests
import xmltodict

def isSprint(race):
    try:
        race['Sprint']
        return True
    except:
        return False

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

    year = 2023
    url = F'http://ergast.com/api/f1/{year}'

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    my_dict = xmltodict.parse(response.text)
    listOfRaces = my_dict['MRData']['RaceTable']['Race']
    ans = f"For {year} season we have:\n"
    for race in listOfRaces:
        ans += f"\nRound {race['@round']}:\n{race['RaceName']}\n"
        if isSprint(race):
            ans += f"Qualifying: {race['Qualifying']['Date']}, {race['Qualifying']['Time']}\n"
            ans += f"Sprint: {race['Sprint']['Date']}, {race['Sprint']['Time']}\n"
        else:
            ans += f"Qualifying: {race['Qualifying']['Date']}, {race['Qualifying']['Time']}\n"
        ans += f"Race: {race['Date']}, {race['Time']}\n"
        
        
    return(ans)