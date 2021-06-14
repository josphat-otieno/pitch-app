
import os


class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    '''
    production configuration child class
    
        Arg:
            Config: th parent configuration class with general configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Test configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
