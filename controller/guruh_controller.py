from flask import Blueprint, render_template, request, redirect, url_for

from model.guruh import Guruh
from service.guruh_service import GuruhService
from service.yunalish_service import YunalishService

gs = GuruhService()
ys = YunalishService()

guruh_url = Blueprint("guruh", __name__, template_folder='../templates')


@guruh_url.route("/guruh", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    if request.method == 'GET':
        tahrirlashId = request.args.get('tahrirlash')
        if tahrirlashId:
            g = gs.getById(tahrirlashId)
            if g:
                return ozgartirish(g)
        return royxat()
    elif request.method == 'POST':
        return qoshish(request.form)
    elif request.method == 'DELETE':
        return ochirish(request.args.get('id'))

def ozgartirish(g):
    guruhlar = gs.getAll()
    yunalishlar = ys.getAll()
    return render_template("guruh.html", guruh = g, guruhlar = guruhlar, yunalishlar = yunalishlar)


@guruh_url.route("/guruh/tahrirlash", methods = ['POST'])
def update():
    g = request.form
    guruh = Guruh(g['nom'], g['yunalish_id'], g['yil'])
    guruh.id = g['id']
    gs.update(guruh)
    return redirect('/guruh')


@guruh_url.route("/guruh/ochirish")
def delete():
    return ochirish(request.args.get('id'))


def royxat():
    guruhlar = gs.getAll()
    yunalishlar = ys.getAll()
    return render_template("guruh.html", guruhlar=guruhlar, yunalishlar=yunalishlar)


def qoshish(g):
    guruh = Guruh(g['nom'], g['yunalish_id'], g['yil'])
    gs.create(guruh)
    return royxat()


def ochirish(id):
    if id:
        gs.deleteById(id)
    return redirect("/guruh")
