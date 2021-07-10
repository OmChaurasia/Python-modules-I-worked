import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

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
    
    # print(fname)
    num=soup.find_all("td", class_="printtextbold")[19].get_text().split()[3]
    zzz=soup.find_all("td", class_="printtextbold")[19].get_text().split()
    p=""
    for i in reversed(zzz):
        if i=="Result":
            break
        else:
            p=f"{i} {p}"
    
    list=[enroll, name, num ,p]
    return list

app = Flask(__name__) 
  

@app.route('/') 
def index(): 
    return render_template('index.html')


@app.route('/', methods=['POST']) 
def getvalue():
    enrolls =  request.form['enrolls']
    enrolls=int(enrolls[1:])
    enrolle =  request.form['enrolle']
    enrolle=int(enrolle[1:])
    print(enrolls, enrolle)
    html='<thead> <tr> <th scope="col">Enrollment Num</th> <th scope="col">Name</th> <th scope="col">Father Name</th> <th scope="col">Marks</th> </tr> </thead> <tbody>'
    for i in range(enrolls,enrolle+1):
        list=marks(f"E{i}")
        
        html =f'{html}<tr> <th scope="row">{list[0]}</th> <td>{list[1]}</td> <td>{list[2]}</td> <td>{list[3]}</td> </tr>'
            
        print(list)
    return render_template('pass.html', val=html )


if __name__ == '__main__': 
    app.run(debug=True) 