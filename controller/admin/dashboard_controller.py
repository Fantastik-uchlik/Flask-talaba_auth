from flask import Blueprint, render_template, request, redirect, url_for

from controller.admin.guruh_controller import guruh_url
from controller.admin.talaba_controller import talaba_url
from controller.admin.yunalish_controller import yunalish_url

admin_url = Blueprint("admin", __name__, template_folder='../../templates/admin')

admin_url.register_blueprint(guruh_url)
admin_url.register_blueprint(talaba_url)
admin_url.register_blueprint(yunalish_url)

@admin_url.route("/admin", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    return render_template("dashboard.html")
