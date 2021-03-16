import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]


class SendEmail:

    def smtp_ssl(self, message, receiver_email):
        import smtplib, ssl
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(params['gmail_user'], params['gmail_password'])
            server.sendmail(params['gmail_user'], receiver_email, message)

    def html_smtp_ssl(self, subject, sender_message, receiver_email):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = params['gmail_user']
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = f"""\
        Hi,
        {sender_message}
        www.python-ds.com"""
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="http://www.python-ds.com">Python DS</a> 
               has many great tutorials.
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(params['gmail_user'], params['gmail_password'])
            server.sendmail(params['gmail_user'], receiver_email, message.as_string())

    def attachments_email_ssl(self, subject, sender_message, receiver_email, filename):
        import email, smtplib, ssl
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"

        sender_email = params['gmail_user']
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = params['gmail_user']
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(sender_message, "plain"))

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(params['gmail_user'], params['gmail_password'])
            server.sendmail(params['gmail_user'], receiver_email, message.as_string())





    def flask_sendgrid(self, message, recipients):
        # pip install Flask-Mail
        from flask import Flask
        from flask_mail import Mail
        from flask_mail import Message

        app = Flask(__name__)

        app.config.update(
            MAIL_SERVER='smtp.sendgrid.net',
            MAIL_PORT=587,
            MAIL_USER_SSL=True,
            MAIL_USERNAME=params['sendgrid_user'],
            MAIL_PASSWORD=params['sendgrid_apikey']
        )
        mail = Mail(app)
        mail.init_app(app)

        msg = Message(message,
                      sender=params['gmail_user'],
                      recipients=recipients
                      )

        # Add more extra filled for attractive email
        # msg.add_recipient("software.vishavjeet26@gmail.com")
        # msg.body = "testing"
        # msg.html = "<b>testing</b>"

        # with app.open_resource("image.png") as fp:
        #     msg.attach("image.png", "image/png", fp.read())

        return mail.send(msg)

    def flask_smpt(self, message, recipients):
        # pip install Flask-Mail
        from flask import Flask
        from flask_mail import Mail
        from flask_mail import Message

        app = Flask(__name__)

        app.config.update(
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=465,
            MAIL_USER_SSL=True,
            MAIL_USERNAME=params['gmail_user'],
            MAIL_PASSWORD=params['gmail_password']
        )
        mail = Mail(app)
        mail.init_app(app)
        msg = Message(message,
                      sender=params['gmail_user'],
                      recipients=recipients
                      )

        # Add more extra filled for attractive email
        # msg.add_recipient("software.vishavjeet26@gmail.com")
        # msg.body = "testing"
        # msg.html = "<b>testing</b>"

        # with app.open_resource("image.png") as fp:
        #     msg.attach("image.png", "image/png", fp.read())
        return mail.send(msg)
