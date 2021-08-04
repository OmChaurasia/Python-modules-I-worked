from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST']) 
def getvalue():
    files= request.files['files']
    files.save(os.path.join("C:\\Users\\user\\Desktop\\study material\\python\\wifi\\recived",files.filename))
    return "File uploaded successfully"

if __name__ == '__main__': 
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=80)