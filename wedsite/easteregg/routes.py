from flask import Blueprint, render_template, url_for, flash, redirect, request

easteregg = Blueprint('easteregg', __name__)

@easteregg.route("/sorpresa")
def sorpresa():
    return render_template("sorpresa.html")

