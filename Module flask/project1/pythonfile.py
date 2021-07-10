from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/coding_blog'
#db = SQLAlchemy(app)

#class Contacts(db.Model):
   # '''
 #   sno, name phone_num, msg, date, email
  #  '''
 #   sno = db.Column(db.Integer, primary_key=True)
 #   name = db.Column(db.String(80), nullable=False)
   # mobile = db.Column(db.String(12), nullable=False)

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/register")
def Register():
    return render_template('register.html')

@app.route("/login")
def Login():
    return render_template('login.html')

@app.route("/about", methods = ['GET', 'POST'])
def About():
  #  if (request.method == 'POST'):
#        '''Add entry to the database'''
    #    name = request.form.get('name')
   #     phone = request.form.get('mobile')
  #      entry = Contacts(name=name, mobile=phone)
   #     db.session.add(entry)
   #     db.session.commit()
    return render_template('about.html')

@app.route("/contact")
def Contact():
    return render_template('contact.html')

app.run(debug=True)