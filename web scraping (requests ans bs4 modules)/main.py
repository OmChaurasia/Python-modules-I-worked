import requests
from bs4 import BeautifulSoup
url= "http://result.bteupexam.in/odd_result/main/oddresult.aspx?Roll_no=E19220735500032"
def fetch(url):
    try:
        r= requests.get(url)
        htmlcontent= r.content
        flag=True
    except:
        flag=False
        htmlcontent=""
    return flag,htmlcontent
i=0
while True:
    flag,content=fetch(url)
    print(i)
    i=i+1
    if (flag==True):
        print(content)
        break

# soup= BeautifulSoup(htmlcontent , 'html.parser')
# print(soup.prettify)

# title= soup.title
# print(title)
# print(title.string)

# anchor= soup.find_all('a')
# print(anchor)
# print(anchor[1])
# print(anchor[1]['class'])
# print(soup.find_all("a", class_="btn"))
# print(anchor[1].get_text())