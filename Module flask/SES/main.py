import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
enrollment_list=['E19220735500002', 'E19220735500020', 'E19220735500027', 'E19220735500025', 'E19220735500005', 'E19220735500032', 'E19220735500003', 'E19220735500019', 'E19220735500028', 'E19220735500029', 'E19220735500001', 'E19220735500009', 'E19220735500061', 'E19220735500013', 'E19220735500022', 'E19220735500046', 'E19220735500049', 'E19220735500023', 'E19220735500006', 'E19220735500036', 'E19220735500037', 'E19220735500012', 'E19220735500035', 'E19220735500053', 'E19220735500045', 'E19220735500024', 'E19220735500021', 'E19220735500050', 'E19220735500011', 'E19220735500033', 'E19220735500030', 'E19220735500055', 'E19220735500031', 'E19220735500039', 'E19220735500062', 'E19220735500015', 'E19220735500010', 'E19220735500043', 'E19220735500066', 'E19220735500042', 'E19220735500044', 'E19220735500008', 'E19220735500041', 'E19220735500067', 'E19220735500018', 'E19220735500038', 'E19220735500026', 'E19220735500017', 'E19220735500004', 'E19220735500051', 'E19220735500057', 'E19220735500058', 'E19220735500056', 'E19220735500048', 'E19220735500007', 'E19220735500034', 'E19220735500016', 'E19220735500059', 'E19220735500060']

def marks(enroll):

    url=f"http://result.bteevaluation.co.in/Odd_Semester/main/result.aspx?Roll_no={enroll}"
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
    
    # print(fname)
    
    num=soup.find_all("td", class_="printtext")[67].get_text().split()[0]
    # print(num)
    # num=soup.find_all("td", class_="printtextbold")[19].get_text().split()[3]
    
    
    list=[enroll, name, num]
    return list

app = Flask(__name__) 
  

@app.route('/') 
def index(): 
    return render_template('index.html')


@app.route('/', methods=['POST']) 
def getvalue():
    
    html='<thead> <tr> <th scope="col">Enrollment Num</th> <th scope="col">Name</th> <th scope="col">Marks</th> </tr> </thead> <tbody>'
    for i in range(59):
        list=marks(f"{enrollment_list[i]}")
      
        html =f'{html}<tr> <th scope="row">{list[0]}</th> <td>{list[1]}</td> <td>{list[2]}</td> </tr>'
            
        print(list)
    return render_template('pass.html', val=html )


if __name__ == '__main__': 
    app.run(debug=True) 