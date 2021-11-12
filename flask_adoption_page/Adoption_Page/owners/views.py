from flask import Blueprint,render_template,redirect,url_for
from Adoption_Page import db
from Adoption_Page.models import Owner
from Adoption_Page.owners.forms import AddForm


owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/owner', methods=['GET', 'POST'])
def addowner():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('owner.html', form=form)