import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.naver.com').text
soup = BeautifulSoup(response, 'html.parser')
tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul .ah_k')
# .ah_k  추가
for tag in tags:
    print(tag.text)

with open('naver.txt', 'w', encoding="utf-8") as f:
    f.write('naver_ranking \n')
    for i, tag in enumerate(tags):
        f.write(f'{i+1}. {tag.text}\n')

# for i, tag in enumerate(tags) : 인덱싱 번호 붙임