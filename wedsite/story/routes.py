from flask import Blueprint, render_template, url_for, flash, redirect, request
from wedsite import db
from wedsite.models import Response
from wedsite.responses.forms import RegistrationForm
import pandas as pd
import numpy as np


story = Blueprint('story', __name__)

@story.route("/our-story")
def our_story():
    return render_template("our_story.html")

