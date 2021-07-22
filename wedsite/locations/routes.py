from flask import Blueprint, render_template, url_for, flash, redirect, request

locations = Blueprint('locations', __name__)

@locations.route("/luoghi")
def luoghi():
    return render_template("luoghi.html")

