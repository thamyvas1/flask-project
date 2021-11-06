from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'



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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


class InfoForm(FlaskForm):

    breed = StringField("What bread are you?")
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
       breed = form.breed.data
       form.breed.data = ''
    return render_template('form.html',form=form, breed=breed)



if __name__ == '__main__':
    app.run(debug=True)
