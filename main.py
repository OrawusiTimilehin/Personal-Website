from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'nviwbv8(*403gjBVEI^@Go2u@f2GU^@%B39(+_!£)BTV'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///projects.db"
db = SQLAlchemy(app)

class Projects(db.Model):
    id = db.Column(db.String(250),primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    github_link = db.Column(db.String(500), unique=True)

app.app_context().push()
class ContactForm(FlaskForm):
    email = EmailField(label="Email:", validators=[DataRequired()])
    name = StringField(label="Name:", validators=[DataRequired()])
    message = StringField(label="Message:", validators=[DataRequired()])
    additional_info = StringField(label="Additional Information:", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

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
            additional_info = data['additional_info']
            return render_template("successful.html")
        else:
            error = "Please Enter in a valid Email"
            return render_template("contact.html", form=contact_form, error=error)

    return render_template("contact.html" , form=contact_form, error=error)


@app.route("/projects/<id>")
def projects(id):
    project_id = id
    project = Projects.query.get(project_id)
    return render_template('projects.html', project=project)


if __name__ == "__main__":
    app.run(debug=True)
