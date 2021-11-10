from flask import Flask, render_template, request,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import (StringField, SubmitField, BooleanField, 
                    DateField, RadioField, SelectField, 
                    TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#main page

@app.route('/')
def index():
    return render_template('puppy.html')


@app.route('/signup')
def signup_form():
    return render_template('signup.html')


@app.route('/thanks')
def thanks():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template('thanks.html', first=first, last=last)

#error handler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#report page

@app.route('/reporthome')
def reporthome():
    return render_template('reporthome.html')


@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get("user")

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('report.html', report=report, lower=lower_letter, upper=upper_letter, numend=num_end)



#@app.route('/puppy/<name>')
#def pup_name(name):
#   return render_template('puppy.html', name=name)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# form

class InfoForm(FlaskForm):

    breed = StringField("What bread are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neuted?")
    mood = RadioField('Please choose your mood:', choices=[('Happy', 'Happy'), ('Excited', 'Excited')])
    food_choice = SelectField('Pick your favorite food:', choices=[('Chicken', 'Chicken'),('Beef', 'Beef'),('Fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Click Me.')

@app.route('/form', methods=['GET', 'POST'])
def form():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
       session['breed'] = form.breed.data
       flash(f"You clicked the button and changed the breed to: {session['breed']}")
       #form.breed.data = ''
       session['neutered']= form.neutered.data
       session['mood'] = form.mood.data
       session['food_choice'] = form.food_choice.data
       session['feedback'] = form.feedback.data
       return redirect(url_for('thankyou'))
    return render_template('form.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
