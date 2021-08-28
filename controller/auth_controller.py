from urllib.parse import unquote

import flask
import flask_login
from flask import Blueprint, request, make_response, render_template, session, url_for
from werkzeug.utils import redirect

from model.user import User
from service.user_service import UserService

auth_url = Blueprint("auth", __name__, template_folder="../templates")
us = UserService()
@auth_url.route("/login", methods=['GET','POST','DELETE','UPDATE'])
def login():
    xabar = request.args.get("xabar")
    next = request.args.get("next")
    # if next is None or next == '' or next == 'None':
    next = "admin.index"
    if request.method == 'POST':
        login = request.form['login']
        parol = request.form['parol']
        user = us.getByLogin(login)
        if user and user.parol == parol:

            res = make_response(redirect(url_for(next)))
            session['login'] = login
            flask_login.login_user(user)
            return res
        else:
            xabar = "Login yoki parolda xatolik"
    return render_template("login.html", xabar=xabar, next = next)



@auth_url.route("/registr", methods=['GET','POST','DELETE','UPDATE'])
def registr():
    xabar = ""
    if request.method == 'POST':
        login = request.form['login']
        ism = request.form['ism']
        familiya = request.form['familiya']
        parol = request.form['parol']
        if login and parol and login and ism and familiya:
            u = User(ism,familiya,login, parol)
            try:
                us.create(u)
                return redirect(url_for("auth.login", xabar="Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi kiring!"))
            except:
                xabar = "Yangi qaytarilmas login kiriting"

        else:
            xabar = "Ro`yxatdan o`tishning iloji bo`lmadi !"
    return render_template("registr.html", xabar=xabar)
@auth_url.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect('/')