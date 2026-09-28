# import requests

# keyword="파이썬"
# url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
# response = requests.get("https://https://www.incruit.com/")
# #print(response.status_code)
# print(requests.text)

import requests
from bs4 import BeautifulSoup

keyword = "파이썬"
# 1. 검색용 URL을 변수에 담습니다.
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
#https://search.incruit.com/list/search.asp?col=job&kw=%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 2. 만든 url 변수를 requests.get()에 전달합니다. (중복 https 수정)
response = requests.get(url)

#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser') # 정상적인 파서 이름
#print(soup.title)
lis = soup.find_all("li",class_="c_col")
#print(lis)
#print(len(lis))

for li in lis:
    company=li.find("a",class_="cpname").text #텍스트는속성값
    location=li.find("div",class_="cl_md").find_all("span")[0].text
    link=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").get("href")
    #print(company)
    #title=li.find("div",class_="cell_mid").find(div",class_="cl_top")).find(a).text
    #print(title)
    #print(location)
    print(link)