# MOVIE_API_KEY = 'bdf96c9ff1dd98a397f61c4e28828a5c'
# SECRET_KEY = 'ramza'

import os


class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
