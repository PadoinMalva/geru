from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from .models.mymodel import DBSession, Base

my_session_factory = SignedCookieSessionFactory ('geru_chalange')
settings = {'sqlalchemy.url': 'sqlite:///./db/geru_challange.sqlite', 'sqlalchemy.echo': 'True'}

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        
        config.set_session_factory(my_session_factory)

        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
