"""Flask configuration variables."""
import os
from os import environ, path

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass import getpass
import pymysql
from google.cloud.sql.connector import Connector, IPTypes

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
    # db_host = os.environ["INSTANCE_HOST"]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    # db_port = os.environ["DB_PORT"]  # e.g. 3306
    # Database
    if os.environ.get("INSTANCE_CONNECTION_NAME"):
        instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
        connector = Connector(ip_type)

        def getconn() -> pymysql.connections.Connection:
            conn: pymysql.connections.Connection = connector.connect(
                instance_connection_name,
                "pymysql",
                user=db_user,
                password=db_pass,
                db=db_name,
            )
            return conn

        pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=getconn,
            # [START_EXCLUDE]
            # Pool size is the maximum number of permanent connections to keep.
            pool_size=5,

            # Temporarily exceeds the set pool_size if no connections are available.
            max_overflow=2,

            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.

            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            pool_timeout=30,  # 30 seconds

            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # re-established
            pool_recycle=1800,  # 30 minutes
            # [END_EXCLUDE]
        )
        url = pool.url
    elif  os.environ.get("INSTANCE_UNIX_SOCKET"):
        unix_socket_path = os.environ["INSTANCE_UNIX_SOCKET"]
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
            sqlalchemy.engine.url.URL.create(
                drivername="mysql+pymysql",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_socket": unix_socket_path},
            ),
            # [START_EXCLUDE]
            # Pool size is the maximum number of permanent connections to keep.
            pool_size=5,

            # Temporarily exceeds the set pool_size if no connections are available.
            max_overflow=2,

            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.

            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            pool_timeout=30,  # 30 seconds

            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # re-established
            pool_recycle=1800,  # 30 minutes
            # [END_EXCLUDE]
        )
        url = pool.url
    else:   # for local test.
        db_host = os.environ["INSTANCE_HOST"]
        db_port = os.environ["DB_PORT"]  # e.g. 3306
        url = sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username='root',
            password='password',
            host=db_host,
            port=db_port,
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