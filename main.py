from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)


class ContactForm(FlaskForm):
    email = EmailField(label="Email:", validators=[DataRequired()])
    name = StringField(label="Name:", validators=[DataRequired()])
    message = StringField(label="Message:", validators=[DataRequired()])
    additional_info = StringField(label="Additional Information:", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
