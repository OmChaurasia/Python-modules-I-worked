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
    num=soup.find_all("td", class_="printtextbold")[19].get_text().split()[3]
    return num

app = Flask(__name__) 
  

@app.route('/') 
def index(): 
    return render_template('index.html')


@app.route('/', methods=['POST']) 
def getvalue():
    name =  request.form['enroll']
    number =  request.form['number']
    num=marks(name)
    if num==number:
        flag="verified"
    else:
        flag="not verified"
    print(num)
    return render_template('pass.html', val=flag )


if __name__ == '__main__': 
    app.run(debug=True) 