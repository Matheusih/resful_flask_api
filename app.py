from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.server.routes import registerBlueprints

from config import config

app = Flask(__name__)
registerBlueprints(app)
app.config.update(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Index page'

if __name__ == '__main__':
    app.run(
        host=app.config['host'],
        port=app.config['port'],
        debug=True
    )
