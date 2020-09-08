from flask import render_template, session, redirect, url_for
from . import hopital
from .forms import AuthentiForm, IndividuForm
from app import db, create_app
from app import models
from ..models import Individu


@hopital.route('/', methods=['GET', 'POST'])
def accueil():
    individus = Individu.query.all()
    form =IndividuForm()
    if form.validate_on_submit():
        individu = Individu(nomI=form.nom.data, prenomI=form.prenom.data, adresseI=form.adresse.data,
                            telephoneI=form.telephone.data, motifI=form.motif.data, sommeI=form.somme.data,
                            numCompte=form.numCompte.data)
        db.session.add(individu)
        db.session.commit()
        return redirect(url_for('hopital.accueil'))
    return render_template('hopital/accueil.html', form=form, individus=individus)


@hopital.route('/presentation')
def presentation():
    return render_template('hopital/presentation.html')


@hopital.route('/authentification')
def authentification():
    return render_template('index.html')
