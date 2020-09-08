from flask import render_template,session,redirect,url_for
from . import admin
from .forms import AuthentiForm
from .. import db 


@admin.route('/login')
def userlogin():
    return render_template('admin/userlogin.html')

@admin.route('/admin/login')
def adminlogin():

    return render_template('admin/adminlogin.html')

@admin.route('/admin/presentation')
def presentation():

    return render_template('admin/presentation.html')

@admin.route('/admin/authentification')
def authentification():

    return render_template('admin/authentification.html')