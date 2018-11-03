#!/usr/bin/env python3
import os

from flask import Flask
from flask import current_app
from flask import g

def register_blueprints(app):
    # Import blueprints
    from views import clothes
    app.register_blueprint(clothes.blueprint, url_prefix="/api/clothes/")


def make_app(config_path=None):
    app = Flask(__name__)
    register_blueprints(app)
    return app


def main():
    app = make_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
