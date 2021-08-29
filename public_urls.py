from datetime import timedelta

import flask_login
from flask import render_template, Blueprint, make_response, request, session

from service.talaba_service import TalabaService
ts = TalabaService()

public_url = Blueprint("",__name__, template_folder='templates')


@public_url.route('/index')
@public_url.route("/")
def index():
    #soni = request.cookies.get("kurishlar")
    soni = session.get("kurishlar")
    if soni:
        soni = int(soni)
        soni += 1
    else:
        soni = 1

    res = make_response(render_template("index.html", kurishlar=soni))
    #res.set_cookie("kurishlar", str(soni), max_age=timedelta(30))
    session['kurishlar'] = str(soni)
    return res
@public_url.route("/talabalar")
def talabalar():

    return render_template("talabalar.html", talabalar=ts.getAll())