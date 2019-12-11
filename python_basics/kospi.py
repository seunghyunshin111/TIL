import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one("#KOSPI_now").text
print(kospi)

# kospi 홈페이지 개발자도구 copy select -> 태그 안 소스만 가져올 수 있음
# .test 붙이면 실제 텍스트만 가져올 수 있음. 