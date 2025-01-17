from flask import Flask
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

@app.route("/")
def index():
    msg = Message(
        # 메일 제목
        subject="SMTP MAIL TEST",
        
        # 발신자
        sender=app.config['MAIL_USERNAME'],

        # 수신자
        recipients=['your_email_address']
    )
    msg.body = "SMTP MAIL TEST"
    mail.send(msg)
    return "Message sent!"


if __name__ == '__main__':
    app.run()