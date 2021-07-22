from flask import Flask
from wedsite.config import Config
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'TOBEFILLED'

################ SQLITE ################
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///site.db'


from wedsite.main.routes import main
from wedsite.responses.routes import responses
from wedsite.wishlist.routes import wishlist
from wedsite.story.routes import story
from wedsite.locations.routes import locations
from wedsite.easteregg.routes import easteregg

app.register_blueprint(main)
app.register_blueprint(responses)
app.register_blueprint(wishlist)
app.register_blueprint(story)
app.register_blueprint(locations)
app.register_blueprint(easteregg)






