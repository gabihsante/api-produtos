from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)

from app.models import produto

db.create_all()


from app.controllers.produto_controller import ProdutoController
app.register_blueprint(ProdutoController.ptoduto_controller, url_prefix="api/v1/")