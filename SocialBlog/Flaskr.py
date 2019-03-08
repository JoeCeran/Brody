from flask import Flask, render_template,session,redirect,url_for,request   
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,SubmitField,
                    RadioField,SelectField,TextField,
                    TextAreaField,SubmitField)     

from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


@app.route("/")
def home():
    return render_template("SignIn.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/signin")
def signin():
    return render_template("SignIn.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('403.html') , 403

if __name__ == "__main__":
    app.run(debug=True)