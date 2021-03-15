from flask import Flask, render_template, request
from datetime import datetime

from db_connection import add_contact, get_contact, delete_contact

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

@app.route("/contact-delete", methods=['POST'])
def contact_delete():
    if (request.method == "POST"):
        results = get_contact()
        id = request.form.get('c_id')
        delete_contact(id)
        return render_template('contact_us_list.html', results={"data": results, "messages": "Record Deleted "
                                                                                             "Successfully!"})
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

        params = {"success": "Thanks for contacting us, our team will coordinate with you soon!",
                  "is_success":True}
        return render_template('contact.html', params=params)
    return render_template('contact.html', params={})

@app.route("/post")
def post():
    return render_template('post.html')

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5555 , debug=True)