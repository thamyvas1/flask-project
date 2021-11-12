from flask import Blueprint,render_template,redirect,url_for
from Adoption_Page import db
from Adoption_Page.models import Puppy
from Adoption_Page.puppies.forms import AddForm,DelForm


puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')


@puppies_blueprint.route('/add', methods=['GET', 'POST'])

def add():

    form = AddForm()

    if form.validate_on_submit():

        pup = form.pup.data
        new_pup = Puppy(pup)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('add.html', form=form)

@puppies_blueprint.route('/list')

def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprint.route('/delete', methods=['GET', 'POST'])

def delete():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('delete.html', form=form)
