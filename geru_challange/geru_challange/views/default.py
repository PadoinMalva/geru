from pyramid.view import view_config
from pyramid.response import Response
import json
from random import choice
from ..helpers.quotes.quotes import get_quotes, get_quote
from ..models.mymodel import GeruChallange

@view_config(route_name='home', renderer='json')
def home(request):
    query = GeruChallange()
    query.save()
    # print(request.headers['COOKIE'])
    # print(request.cookies)
    # print(request.url)
    return Response('Desafio Web 1.0')


@view_config(route_name='quotes', renderer='json')
def quotes(request):
    print(request.headers['COOKIE'])
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

