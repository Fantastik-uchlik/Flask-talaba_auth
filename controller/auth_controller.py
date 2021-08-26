from flask import Blueprint, request, make_response, render_template, session
from werkzeug.utils import redirect

from model.user import User
from service.user_service import UserService

auth_url = Blueprint("login", __name__, template_folder="../templates")
us = UserService()
@auth_url.route("/login", methods=['GET','POST','DELETE','UPDATE'])
def login():
    xabar = ""
    if request.method == 'POST':
        login = request.form['login']
        parol = request.form['parol']
        user = us.getByLogin(login)
        if user and user.parol == parol:
            res = make_response(redirect("/talaba"))
            session['login'] = login
            return res
        else:
            xabar = "Login yoki parolda xatolik"
    return render_template("login.html", xabar=xabar)



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
            us.create(u)
            return redirect('/login')

        else:
            xabar = "Ro`yxatdan o`tishning iloji bo`lmadi !"
    return render_template("registr.html", xabar=xabar)