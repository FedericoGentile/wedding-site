from flask import Blueprint, render_template, url_for, flash, redirect, request
from wedsite import db
from wedsite.models import Response
from wedsite.responses.forms import RegistrationForm


responses = Blueprint('responses', __name__)

@responses.route("/rsvp-info",methods=['GET', 'POST'])
def rsvp_info():
    form = RegistrationForm()
    if form.validate_on_submit():
        response = Response(username=form.username.data,
                            lastname=form.lastname.data,
                            email=form.email.data, 
                            adults=form.adults.data,
                            children=form.children.data,
                            message=form.message.data,
                            accomodation=form.accomodation.data)
        db.session.add(response)
        db.session.commit()
        flash(f"La risposta e' stata inoltrata correttamente!", 'success')
        return redirect(url_for('responses.rsvp_info'))
    else:
        if form.is_submitted()==True and form.validate()==False:
            flash(f"Il form non e' stato compilato correttamente!", 'danger')
    return render_template("rsvp_info.html", title="RSVP & Info - Federico & Maria", form=form)

