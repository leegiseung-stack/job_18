import requests
from bs4 import BeautifulSoup
location = "정보 없음"

def search_incruit(keyword, pages=1):
    jobs = []
    for page in range(pages):
        page = page * 30

        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        for li in lis:
            company = li.find("a", class_="cpname").text
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
            location = li.find("div", class_="cl_md").find_all("span")[0].text
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")

            job_data = {
                "company" : company, 
                "title": title, 
                "location": location, 
                "link": link,
                "source": "인크루트"
            }
            jobs.append(job_data)   

    return jobs


def work24(keyword, pages=1):
    jobs = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(1, pages + 1):
        url = f"https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do?srcKeyword={keyword}&pageIndex={page}&resultCnt=30&sortField=DATE&sortOrderBy=DESC"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # 공고 1개 = <tr id="list1">, <tr id="list2"> ...
        rows = soup.select("tr[id^=list]")

        for tr in rows:
            company_tag = tr.select_one("a.cp_name")       # 어니스트에이아이
            title_tag = tr.select_one("a.t3_sb")           # Software Engineer, Backend (BaaS)
            location_tag = tr.select_one("li.site p")      # 서울 강남구

            if title_tag is None:
                continue

            company = company_tag.get_text(strip=True) if company_tag else "정보 없음"
            title = title_tag.get_text(" ", strip=True)
            location = location_tag.get_text(" ", strip=True) if location_tag else "정보 없음"

            href = title_tag.get("href", "")
            link = href if href.startswith("http") else "https://www.work24.go.kr" + href

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link,
                "source": "고용24",
            }
            jobs.append(job_data)

    return jobs

def search_all(keyword, pages=1):
    jobs = []
    for func in (search_incruit, work24):
        try:
            jobs += func(keyword, pages)
        except Exception as e:
            print(f"{func.__name__} 오류: {e}")
    return jobs