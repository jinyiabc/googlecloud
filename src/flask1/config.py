"""Flask configuration variables."""
import os
from os import environ, path

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass import getpass

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # # General Config
    # SECRET_KEY = environ.get("SECRET_KEY")
    # FLASK_APP = environ.get("FLASK_APP")
    # FLASK_ENV = environ.get("FLASK_ENV")
    # Get database address.
    # db_addr = input("DB ip address: ")
    # # Get username of the database.
    # db_user = input(f"Username of {db_addr}: ")
    # # Get password.
    # db_pass = getpass(f"Password of {db_user}@{db_addr}: ")
    # # Get the database name.
    # db_name = input("Database name to connect: ")
    #
    # # join the inputs into a complete database url.
    # url = f"mysql+pymysql://{db_user}:{db_pass}@{db_addr}/{db_name}"

    # Create an engine object.
    # engine = create_engine(url, echo=True)
    #
    # # Create database if it does not exist.
    # if not database_exists(engine.url):
    #     create_database(engine.url)
    # else:
    #     # Connect the database if exists.
    #     engine.connect()
    db_host = os.environ["MYSQL_DB_HOST"]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    # db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    # db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    # db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    # db_port = os.environ["DB_PORT"]  # e.g. 3306
    # Database
    url = sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username='root',
        password='password',
        host=db_host,
        port=3306,
        database='mydb',
    )

    # Create an engine object.
    engine = create_engine(url, echo=True)

    # Create database if it does not exist.
    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        # Connect the database if exists.
        # engine.connect()
        pass


    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "random string"