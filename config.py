class Config(object):

    #Secret key
    SECRET_KEY = 'my_very_secret_key'

    ITEMS_PER_PAGE = 25

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'