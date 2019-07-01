from pyramid.view import view_config
from pyramid.response import Response
import json
from random import randrange
import transaction
from ..helpers.quotes.quotes import get_quotes, get_quote
from ..models.mymodel import SessionLog, DBSession
from ..helpers.identifier.identifier import random_string
from ..helpers.decorators.decorator_get import get_check
import datetime

def check_session(session, url):
    check_session = session
    if 'identifier' in session.keys():
        print('ID Session existente')
    else:
        print('Criando ID Session')
        check_session['identifier'] = random_string()

    DBSession.add(SessionLog(identifier=check_session['identifier'], url=url))
    transaction.commit()

    return check_session


@view_config(route_name='home', renderer='./templates/home.jinja2')
def home(request):
    session = check_session(request.session, request.url)
    return dict(title='Desafio Web 1.0!')


@view_config(route_name='quotes', renderer='./templates/quotes.jinja2')
def quotes(request):
    session = check_session(request.session, request.url)
    quotes = get_quotes()
    return quotes

@view_config(route_name='quotes_number', renderer='./templates/quotes_number.jinja2')
def quotes_number(request):
    session = check_session(request.session, request.url)
    quote_number = request.matchdict
    response = get_quote(quote_number['first'])
    response['quote_number'] = quote_number['first']
    return response
    
@view_config(route_name='quotes_random', renderer='./templates/quotes_number.jinja2')
def quotes_random(request):
    session = check_session(request.session, request.url)
    random_quotes = get_quotes()
    random_index = randrange(len(random_quotes['quotes']))
    response = {
        'quote_number':random_index,
        'quote': random_quotes['quotes'][random_index]
    }
    return response

@view_config(route_name='session_log', renderer='json')
@get_check
def session_log(request):
    for x in request.headers:
        print(x)
    retorno = DBSession.query(SessionLog).all()
    response_obj=list()
    for session_obj in retorno: 
        response_obj.append( {
            'identifier':session_obj.identifier,
            'url':session_obj.url,
            'datahora':session_obj.datahora.isoformat()
        })

    response = json.dumps(response_obj)
    return Response(json_body=json.loads(response))
