import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from adoption_form import AddForm, DelForm, AddOwnerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#####################
### SQL DATABASE ###
####################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)  # connect the database


#####################
###### MODELS ######
####################

class Puppy(db.Model):

    ##Manual override tablename##
    __tablename__ = 'puppy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    owner = db.relationship('Owner', backref='puppy', uselist = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self): 
        if self.owner:
            return f"Puppy {self.name} has a owner called {self.owner.name}"
        else:
            return f"Puppy {self.name} has no owner yet!!"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self,name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


#####################
###VIEW FUNCTIONS ###
#####################

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():

        pup = form.pup.data

        new_pup = Puppy(pup)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

@app.route('/owner', methods=['GET', 'POST'])
def addowner():

    form = AddOwnerForm()

    if form.validate_on_submit():

        id = form.id.data
        owner = Owner.query.get(id)
        db.session.add(owner)
        db.session.commit()

        #return redirect(url_for('list_pup'))
    return render_template('owner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)