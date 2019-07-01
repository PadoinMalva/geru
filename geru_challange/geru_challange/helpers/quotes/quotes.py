# -*- coding: utf-8 -*-
import requests
import json

url = '''https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'''

def get_quotes():
    quotes = requests.get(url)
    response = json.loads(quotes.text)
    return response

def get_quote(quote_number):
    quote = requests.get(url+'/'+quote_number)
    response = json.loads(quote.text)
    return response