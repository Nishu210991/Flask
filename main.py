from flask import Flask, render_template, request
from datetime import datetime
from flask_mail import Mail

from db_connection import add_contact, get_contact, delete_contact, get_post

app = Flask(__name__)

app.config.update(
   MAIL_SERVER= 'smtp.sendgrid.net',
   MAIL_PORT= 465,
   MAIL_USER_SSL= True,
   MAIL_USERNAME=  "smtp.sendgrid.net'",
   MAIL_PASSWORD= "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",
)

mail= Mail(app)

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

        mail.send_message('New message from ',
                          sender="python.ds.com@gmail.com",
                          recipients="singh.vishavjeet11@gmail.com",
                          body="message",
                          )
        params = {"success": "Thanks for contacting us, our team will coordinate with you soon!",
                  "is_success":True}
        return render_template('contact.html', params=params)
    return render_template('contact.html', params={})

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post=get_post(post_slug)
    return render_template('post.html' , post=post)

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5555 , debug=True)