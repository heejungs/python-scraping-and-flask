import requests
from bs4 import BeautifulSoup


def data_infor(trs,lists,dic):
    for tr in trs[::-1]: # 0203부터 출력하기 위해 끝에서부터 조회
        infor = {}
        td = tr.find('td') #td안에 있는 date text 
        span = tr.find_all('span') # span안에 있는 case와 death text
        case_num = span[0].text # span안에 있는 case와 death 정보 분리
        case_per = span[1].text
        case = case_num + case_per # case의 정보
        death_num = span[2].text
        death_per = span[3].text
        death = death_num+death_per  # death의 정보

        infor['Date'] = td.text # dic에 각 정보들 삽입
        infor['cases'] = case
        infor['death'] = death
        lists.append(infor)
    return lists

def call_data_info():

    url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Korea'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find("div",{'class':'barbox tright'})

    lists=[]
    dic = {}
    trs = results.find_all('tr')[-2:-17:-1]  # 0203~0217의 tr만을 가져오기 위해 슬라이싱
    # 스크래핑 정보 name 표시

    return data_infor(trs,lists,dic)
    
print(call_data_info())