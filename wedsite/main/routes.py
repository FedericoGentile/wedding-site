from flask import Blueprint
from flask import redirect, render_template, url_for, flash

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")