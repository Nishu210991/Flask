from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Scorpions'
# code canbe copied from https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    phone_num = db.Column(db.String(20), nullable=False)
    mes = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(20),  nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact(request):
    if (request.method == "POST"):

        '''Add Entry to the Database'''
        name  = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message=request.form.get('message')
    #---Database field_name= sno, name, email, phone_num, msg, date
        entry = Contacts(name='name', email='email', phone_num='phone', msg='message', date= datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

#app.run(debug=True)

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5555 , debug=True)
    # automatically change show on broswer if debug=True.Don't need to reload the page.