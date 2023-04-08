from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nviwbv8(*403gjBVEI^@Go2u@f2GU^@%B39(+_!£)BTV'
Bootstrap(app)


class ContactForm(FlaskForm):
    email = EmailField(label="Email:", validators=[DataRequired()])
    name = StringField(label="Name:", validators=[DataRequired()])
    message = StringField(label="Message:", validators=[DataRequired()])
    additional_info = StringField(label="Additional Information:", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


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

if __name__ == "__main__":
    app.run(debug=True)
