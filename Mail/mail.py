from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('yeahhhhhhhh', sender = 'aprabakar476@gmail.com', recipients = ['id1@gmail.com'])
   msg.body = "Hey I done sending mail from python code:)"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)