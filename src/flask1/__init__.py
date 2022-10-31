"""Initialize Flask app."""
import os

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

from .connect_connector import connect_with_connector
from .connect_tcp import connect_tcp_socket
from .connect_unix import connect_unix_socket

# def init_connection_pool() -> sqlalchemy.engine.base.Engine:
#     # use a TCP socket when INSTANCE_HOST (e.g. 127.0.0.1) is defined
#     if os.environ.get("INSTANCE_HOST"):
#         return connect_tcp_socket()
#
#     # use a Unix socket when INSTANCE_UNIX_SOCKET (e.g. /cloudsql/project:region:instance) is defined
#     if os.environ.get("INSTANCE_UNIX_SOCKET"):
#         return connect_unix_socket()
#
#     # use the connector when INSTANCE_CONNECTION_NAME (e.g. project:region:instance) is defined
#     if os.environ.get("INSTANCE_CONNECTION_NAME"):
#         return connect_with_connector()
#
#     raise ValueError(
#         "Missing database connection type. Please define one of INSTANCE_HOST, INSTANCE_UNIX_SOCKET, or INSTANCE_CONNECTION_NAME"
#     )


# # create 'votes' table in database if it does not already exist
# def migrate_db(db: sqlalchemy.engine.base.Engine) -> None:
#     with db.connect() as conn:
#         conn.execute(
#             "CREATE TABLE IF NOT EXISTS votes "
#             "( vote_id SERIAL NOT NULL, time_cast timestamp NOT NULL, "
#             "candidate VARCHAR(6) NOT NULL, PRIMARY KEY (vote_id) );"
#         )

db = SQLAlchemy()

def create_app():
    # """Construct the core application."""
    # app = Flask(__name__)
    # app.config.from_object("config.Config")
    #
    # db.init_app(app)
    #
    # with app.app_context():
    #     from . import routes  # Import routes
    #
    #     db.create_all()  # Create database tables for our data models
    #
    #     return app

    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    # logger = logging.getLogger()
    # db = None
    # global db
    # db = init_connection_pool()
    # migrate_db(db)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        return app