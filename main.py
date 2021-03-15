from flask import Flask, render_template, request
from datetime import datetime
from flask_mail import Mail
from flask_mail import Message

from db_connection import add_contact, get_contact, delete_contact, mysql_db

app = Flask(__name__)

app.config.update(
   MAIL_SERVER= 'localhost',
   MAIL_PORT= 25,
   MAIL_USER_SSL= False,
   MAIL_USERNAME=  "root",
   MAIL_PASSWORD= ""
)
mail= Mail(app)
mail.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact-list", methods=['GET'])
def contact_list():
    results=get_contact()
    return render_template('contact_us_list.html', results={"data":results, "messages":""})

@app.route("/contact-delete", methods=['POST', 'GET'])
def contact_delete():
    if (request.method == "POST"):
        id = request.form.get('c_id')
        delete_contact(id)

        if (delete_contact):
            results = get_contact()
            return render_template('contact_us_list.html', results={"data": results, "messages": "Record Deleted "
                                                                                              "Sucessfully"})

    return render_template('contact_us_list.html', results= {"data":get_contact()})

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if (request.method == "POST"):
        name  = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message=request.form.get('message')

        sql = "INSERT INTO contacts (name, email, phone_num, msg, date) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email ,phone ,message, datetime.now())
        add_contact(sql, val)

        msg = Message("Hello",
                      sender="from@example.com",
                      recipients=["to@example.com"])
        print(msg)
        mail.send(msg)

        params = {"success": "Thanks for contacting us, our team will coordinate with you soon!",
                  "is_success":True}
        return render_template('contact.html', params=params)
    return render_template('contact.html', params={})

@app.route("/post")
def post():
    return render_template('post.html')

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5555 , debug=True)