from flask import Flask, render_template, url_for, redirect, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import ssl
import smtplib
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'nviwbv8(*403gjBVEI^@Go2u@f2GU^@%B39(+_!£)BTV'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://personal_website_db_buow_user:HCdE4WP31pP9MrKyMSk92gEOajOzPSPR@dpg-ciesoc6nqql22ekofckg-a.oregon-postgres.render.com/personal_website_db_buow"
db = SQLAlchemy(app)


#  postgresql://personal_website_db_buow_user:HCdE4WP31pP9MrKyMSk92gEOajOzPSPR@dpg-ciesoc6nqql22ekofckg-a.oregon-postgres.render.com/personal_website_db_buow

class Projects(db.Model):
    id = db.Column(db.String(250),primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    github_link = db.Column(db.String(500), unique=True)
    youtube_url = db.Column(db.String(500), unique=True)

app.app_context().push()
class ContactForm(FlaskForm):
    email = EmailField(label="Email:", validators=[DataRequired()])
    name = StringField(label="Name:", validators=[DataRequired()])
    message = StringField(label="Message:", validators=[DataRequired()])
    additional_info = StringField(label="Additional Information:", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

# db.create_all()


@app.route("/")
def home():
    return render_template("index.html", home=True)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    contact_form = ContactForm()
    error = None
    if request.method == 'POST':
        data = request.form
        if '@' in data['email']:
            email = data['email']
            name = data['name']
            message = data['message']  
            
            

            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "timipythontesting@gmail.com"
            receiver_email = "oluwatimilehin.orawusi@gmail.com"
            password = "ojdsxfzcmcnzmvds"
            message = f"""
            Subject: Contact Me Info


            Name: {name}\nEmail: {email}\nMessage: {message}"""


            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            return render_template("successful.html")
        else:
            error = "Please Enter in a valid Email"
            return render_template("contact.html", form=contact_form, error=error)
         
    return render_template("contact.html" , form=contact_form, error=error, home=False)


@app.route("/projects/<id>")
def projects(id):
    project_id = id
    project = Projects.query.get(project_id)
    shorts = False
    availability = True
    if project_id =="3":
        shorts= True
    elif project_id==1:
        availability = False
    else:
        pass

    return render_template('projects.html', project=project, home=False, shorts=shorts, available=availability, project_id=project)

@app.route("/cv")
def cv():
    return send_file("static/Oluwatimilehin CV Modified 2.pdf")


if __name__ == "__main__":
    app.run(debug=True)
