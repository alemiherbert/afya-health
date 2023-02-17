from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    """
    This is the basic configuration for the database
    Current design choices are
    1. SQLite database
    Final prodict design choices
    1. MySQL database
    """
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") or \
        f"sqlite:///{path.join(basedir, 'db.sqlite3')}"
