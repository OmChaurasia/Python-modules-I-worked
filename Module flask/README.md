## Basic Folders and main file
- static
- templates
- main.py

# Quick start cheatsheet

```
from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/') 
def index(): 
    # return "<h1>hello world</h1>"
    return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True) 
    # app.run(host='0.0.0.0',port=80)
```

# Jinja Templates
```
@app.route('/') 
def index(): 
    return render_template('index.html', val=flag )
```
- Passing the value in index.html file ``<h3>hello {{val}}</h3>``
- Passing the safe html using jinja ``<h3>hello {{val|safe}}</h3>``

# Form Submitting
- In action you can write `/ or /process or which route you are defining
```
@app.route('/', methods=['POST']) 
def getvalue():
    value1 =  request.form['input_box_name1']
    value2 =  request.form['input_box_name2']
    return render_template('pass.html', val=value1 )
```
### Submitting files
```
@app.route('/', methods=['POST']) 
def getvalue():
    files= request.files['files']
    files.save(os.path.join("C:\\Users\\user\\Desktop\\study material\\python\\wifi\\recived",files.filename))
    return "File uploaded successfully"
```
- You need to import os module
- In this function you can check login and save it in database if needed.

## AJAX form submitting
```
@app.route('/process', methods=['POST']) 
def getvalue():
    text =  request.get_json()['textbox']
    # print(text)
    return jsonify({"Ans": ans , "file":speak})
```
- you need to import `jsonify` from flask
### JS fetch api ajax post request
```
var form = document.getElementById("myForm")

form.addEventListener('submit',function(e){
    textbox=document.getElementById('textbox').value
    data={
        "textbox" : textbox
    }
    console.log(data)
    e.preventDefault()
    fetch("/process",
    {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
          }
    })
    .then(response => response.json())
    .then((data) => {
        console.log(data)
    })
    .catch(e=> alert("error"))
})
```
- **In the same way we can create API using flask**