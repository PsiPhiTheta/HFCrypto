import requests
import sys
import time
from bs4 import BeautifulSoup


url = 'https://github.com/gridcoin/Gridcoin-Research'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

output = soup.find("span", {"class": "text-emphasized"}).get_text(strip=True)

# sys.stdout = data.txt
# print output.prettify()
# time.sleep(300)
print output