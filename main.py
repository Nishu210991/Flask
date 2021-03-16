from flask import Flask, render_template, request
from datetime import datetime
from flask_mail import Mail
from flask_mail import Message


from db_connection import add_contact, get_contact, delete_contact, mysql_db, get_post
from emailer import SendEmail

app = Flask(__name__)



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
        success_message= "Thanks for contacting us, our team will coordinate with you soon!"

        params = {"success": success_message, "is_success":True}
        # Email Trigger
        sendEmail = SendEmail()

        # sendEmail.smtp_ssl(message, email)

        # sendEmail.html_smtp_ssl("New Enquiry", message, email)

        filename = "rent-agreement-vishavjeet.pdf"
        sendEmail.attachments_email_ssl("New Enquiry", message, email, filename)


        #sendEmail.flask_smpt(success_message, [email])
        # sendEmail.flask_sendgrid(success_message, [email])

        return render_template('contact.html', params=params)
    return render_template('contact.html', params={})

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post=get_post(post_slug)
    return render_template('post.html' , post=post)

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5555 , debug=True)