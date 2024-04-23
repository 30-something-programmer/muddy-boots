import json
import logging
import flask
import os
from flask import Flask, url_for, redirect, request
from flask_cors import CORS
from modules.config import config
from modules.runtime import get_base_path

log = logging.getLogger("werkzeug")
log.setLevel(logging.INFO)

def website_server():
    """Host an interface to allow access to webfiles. Makes a website"""
    
    try:
        website_folder = get_base_path() / "website"
        templates_folder = os.path.join(website_folder, 'html')
        server = Flask("Muddy Boots Website", static_folder = website_folder, template_folder = templates_folder)
        CORS(server)

        # Set the default route to redirect to dash
        @server.route("/")
        def Root():
            return redirect(url_for('Index'))

        # Dashboard website
        @server.route("/index", methods=["GET"])
        def Index():
            return flask.render_template("index.html")

        # Run the webserver
        server.run(
            debug = config["website"]["debug"], 
            threaded = True, 
            host = config["website"]["host"], 
            port = config["website"]["port"],
            use_reloader = False
        )

    except Exception as e:
        log.debug(str(e))