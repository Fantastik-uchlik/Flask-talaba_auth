import flask_login
from flask import Blueprint, render_template, request, redirect, url_for

from model import Yunalish
from service.yunalish_service import YunalishService

ys = YunalishService()

yunalish_url = Blueprint("yunalish", __name__, template_folder='../templates')


@yunalish_url.route("/yunalish", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
@flask_login.login_required
def index():
    if request.method == 'GET':
        tahrirlashId = request.args.get('tahrirlash')
        if tahrirlashId:
            y = ys.getById(tahrirlashId)
            if y:
                return ozgartirish(y)
        return royxat()
    elif request.method == 'POST':
        return qoshish(request.form)
    elif request.method == 'DELETE':
        return ochirish(request.args.get('id'))


@yunalish_url.route("/yunalish/ochirish")
@flask_login.login_required
def delete():
    return ochirish(request.args.get('id'))

@yunalish_url.route("/yunalish/tahrirlash", methods=['POST'])
@flask_login.login_required
def update():
    y = request.form
    yunalish = Yunalish(y['nom'], y['kod'], y['izoh'])
    yunalish.id = y['id']
    ys.update(yunalish)
    return redirect("/yunalish")








def royxat():
    yunalishlar = ys.getAll()
    return render_template("yunalish.html", yunalishlar=yunalishlar)


def qoshish(y):
    yunalish = Yunalish(y['nom'], y['kod'], y['izoh'])
    ys.create(yunalish)
    return royxat()


def ochirish(id):
    if id:
        ys.deleteById(id)
    return redirect("/yunalish")

def ozgartirish(y):
    yunalishlar = ys.getAll()
    return render_template("yunalish.html", yunalish=y, yunalishlar=yunalishlar)