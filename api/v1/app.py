#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(
        host=os.getenv('HBNB_API_HOST'),
        port=os.getenv('HBNB_API_PORT'),
        threaded=True)
