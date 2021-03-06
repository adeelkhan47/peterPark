from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from api import blueprint
from model.base import db

app = Flask(__name__, static_folder="../static")

app.register_blueprint(blueprint, url_prefix="/api/v1/")

app.config["CORS_HEADERS"] = "Content-Type"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@PeterPark_DB:5432/peterPark"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)

app.app_context().push()
migrate = Migrate(app, db)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=500)
