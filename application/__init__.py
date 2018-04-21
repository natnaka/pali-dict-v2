# encoding: utf-8
import os
import sys
from flask import (Flask, request, url_for,
                   g, render_template, session,
                   jsonify, Blueprint, make_response)
from werkzeug.contrib.fixers import ProxyFix

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from config import load_config

def create_app():
    config = load_config()

    app = Flask(__name__)
    app.config.from_object(config)

    # Proxy Fix
    app.swgi_app = ProxyFix(app.wsgi_app)

    # Register components
    register_db(app)
    register_routes(app)

    return app

def _import_submodules_from_package(package):
    import pkgutil

    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,prefix=package.__name__+"."):
        modules.append(__import__(modname, fromlist="dummy"))
    return modules

def register_routes(app):
    """Register routes."""
    from . import controllers
    from flask.blueprints import Blueprint

    for module in _import_submodules_from_package(controllers):
        bp = getattr(module, 'bp')
        if bp and isinstance(bp, Blueprint):
            app.register_blueprint(bp)

def register_db(app):
    """Register db orm."""
    from .models import db
    db.init_app(app)
