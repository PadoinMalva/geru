from pyramid.view import view_config
from pyramid.response import Response
import json
from random import choice
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


@view_config(route_name='home', renderer='json')
def home(request):
    session = check_session(request.session, request.url)
    return Response('Desafio Web 1.0')


@view_config(route_name='quotes', renderer='json')
def quotes(request):
    session = check_session(request.session, request.url)
    quotes = get_quotes()
    return quotes['quotes']

@view_config(route_name='quotes_number', renderer='json')
def quotes_number(request):
    print(request.url)
    quote_number = request.matchdict
    response = get_quote(quote_number['first'])
    print(response)
    return response['quote']
    
@view_config(route_name='quotes_random', renderer='json')
def quotes_random(request):
    random_quotes = get_quotes()
    return choice(random_quotes['quotes'])

@view_config(route_name='session_log', renderer='json')
@get_check
def session_log(request):
    print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<',request.method)
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
