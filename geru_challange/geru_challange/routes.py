def includeme(config):
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('static', 'static', cache_max_age=3600 )
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quotes_random', '/quotes/random')
    config.add_route('quotes_number', '/quotes/{first}')
    
