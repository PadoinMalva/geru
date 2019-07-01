# Geru Challend
Insert description here

## Requirements
- Unix System
- Python 3.6+
- Python3 pip

## Setting Up
Create virtualenv

bash 
python3 -m venv venv
source venv/bin/activate


install dependencies
bash
python3 setup.py develop


## Running the project
bash
pserve development.ini

## Running Tests(working on it)
bash
pytest

## Site URLS
- home

    url:localhost/

- quotes: show a list of quotes

    url:localhost/quotes

- random_quote: show a random quote

    url:localhost/quotes/random

- quote (specific): show the quote selected by the user 

    url:localhost/quotes/{number of desire quote}

## Endpoint

-- Session Logs

    Method ('GET')
    localhost/sessionlogs
    
    return a Json

    Json example: [
        {
            'identifier':string,
            'url':string,
            'datahora':string
        },
        {
            'identifier':string,
            'url':string,
            'datahora':string
        }
    ]

