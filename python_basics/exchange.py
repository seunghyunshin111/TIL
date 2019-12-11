import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(response, 'html.parser')
select = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(select)