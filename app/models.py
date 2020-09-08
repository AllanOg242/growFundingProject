from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from app import login_manager, admin_login_manager


class Profil(db.Model):
    __tablename__ = 'profils'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(64), index=True)
    users = db.relationship('User', backref='profil', lazy='dynamic')

    def __repr__(self):
        return f'<Profil {self.libelle}>'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64), )
    telephone = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True, index=True)
    mdp = db.Column(db.String(20), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribue')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    profil_id = db.Column(db.Integer, db.ForeignKey('profils.id'))
    individus = db.relationship('Individu', backref='user', lazy='dynamic')
    virements = db.relationship('Virement', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.nom}-{self.email}-{self.mdp}-{self.telephone}>'


class Individu(db.Model):
    __tablename__ = 'individus'
    id = db.Column(db.Integer, primary_key=True)
    nomI = db.Column(db.String(64), )
    prenomI = db.Column(db.String(64))
    telephoneI = db.Column(db.String(64), unique=True, index=True)
    motifI = db.Column(db.String(64))
    sommeI = db.Column(db.String(64), index=True)
    adresseI = db.Column(db.String(20), index=True)
    numCompte = db.Column(db.String(20), unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    typeindividu_id = db.Column(db.Integer, db.ForeignKey('typeindividus.id'))
    virements_id = db.Column(db.Integer, db.ForeignKey('virements.id'))
    dossier_id = db.Column(db.Integer, db.ForeignKey('dossiers.id'))

    def __repr__(self):
        return f'<Individu {self.numCompte}-{self.nomI}-{self.prenomI}-{self.adresseI}>'


class Virement(db.Model):
    __tablename__ = 'virements'
    id = db.Column(db.Integer, primary_key=True)
    montantV = db.Column(db.Integer)
    dateV = db.Column(db.String(64))
    numCompteV = db.Column(db.String(64), unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    individus = db.relationship('Individu', backref='virement')

    def __repr__(self):
        return f'<Virement {self.numCompteV}-{self.montantV}-{self.dateV}>'


class Typeindividu(db.Model):
    __tablename__ = 'typeindividus'
    id = db.Column(db.Integer, primary_key=True)
    libelleT = db.Column(db.String(20))
    individus = db.relationship('Individu', backref='typeindividus', lazy='dynamic')

    def __repr__(self):
        return f'<Typeindividu {self.libelleT}>'


class Dossier(db.Model):
    __tablename__ = 'dossiers'
    id = db.Column(db.Integer, primary_key=True)
    numeroD = db.Column(db.Integer)
    dateCr = db.Column(db.String(64))
    individus = db.relationship('Individu', backref='dossier', lazy='dynamic')
    verification_id = db.Column(db.Integer, db.ForeignKey('verifications.id'))

    def __repr__(self):
        return f'<Dossier {self.numeroD}-{self.dateCr}>'


class Verification(db.Model):
    __tablename__ = 'verifications'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64))
    reponse = db.Column(db.String(64))
    dossiers = db.relationship('Dossier', backref='verification')

    def __repr__(self):
        return f'<Verification {self.reponse}-{self.date}>'

'''
@login_manager.user_loader()
def load_user(user_id):
    return User.query.get(int(user_id))


@admin_login_manager.user_loader
def load_admin(admin_id):
    return User.query.get(int(admin_id))
'''