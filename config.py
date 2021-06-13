
import os


class Config:
    '''
    general configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/pitch'

class ProdConfig(Config):
    '''
    production configuration child class
    
        Arg:
            Config: th parent configuration class with general configuration settings
    '''

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
