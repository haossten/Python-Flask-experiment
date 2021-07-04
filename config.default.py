class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<user>:<password>@<host>/<database>'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://<user>:<password>@<host>/<database>'