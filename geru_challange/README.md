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
bash
localhost/

- quotes: show a list of quotes
bash
localhost/quotes

- random_quote: show a random quote
bash
localhost/quotes/random

- quote (specific): show the quote selected by the user 
bash
/quotes/{desire quote number}
