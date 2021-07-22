from flask import Blueprint, render_template, url_for, flash, redirect, request
from wedsite import db
from wedsite.models import Response
from wedsite.responses.forms import RegistrationForm
import pandas as pd
import numpy as np


wishlist = Blueprint('wishlist', __name__)

@wishlist.route("/lista-nozze")
def lista_nozze():
    lista = pd.read_excel("C:/Users/feder/OneDrive/Matrimonio/lista_nozze/lista_nozze.xlsx").dropna(subset=['oggetto']).reset_index(drop=True)
    print(lista[['descrizione']])
    lista[['prezzo','ratio']] = lista[['prezzo','ratio']].astype(int)
    n_rows = int(np.ceil(lista.shape[0]/3))
    return render_template("lista_nozze.html", title="Lista Nozze - Federico & Maria", lista=lista, n_rows=n_rows)

