import requests
import sys
import time
from bs4 import BeautifulSoup

def returnResult():
    url = 'https://github.c/gridcoin/Gridcoin-Research'
    try:
        response = requests.get(url)
        html = response.content
    except:
        result = []
        for i in range(0, 5):
            result.append(float('nan'))
        return result

    soup = BeautifulSoup(html, 'html.parser')

    output = soup.find("span", {"class": "text-emphasized"}).get_text(strip=True)
    print("githubParser: " + str(len(output)))
    return(output)
