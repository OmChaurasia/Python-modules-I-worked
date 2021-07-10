import requests
from bs4 import BeautifulSoup

def marks(enroll):
    url=f"http://result.bteupexam.in/odd_result/main/oddresult.aspx?Roll_no={enroll}"
    # print(url)
    r= requests.get(url)
    htmlcontent= r.content
    soup= BeautifulSoup(htmlcontent , 'html.parser')
    # print(soup)
    nameandfname=soup.find_all("td", class_="printtext")[4].get_text().split()
    name=""
    fname=""
    for i in nameandfname:
        if i=="Father":
            break
        else:
            name=f"{name} {i}"
    for i in reversed(nameandfname):
        if i==":":
            break
        else:
            fname=f"{i} {fname}"
    # print(fname)
    num=soup.find_all("td", class_="printtextbold")[19].get_text().split()[3]
    list=[enroll, name, fname ,num]
    return list
# list=marks("E19220735500001")
for i in range(19220735600001,19220735600068):
    list=marks(f"E{i}")
    print(list)