def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = environ['QUERY_STRING'][2:]
    return url.replace('&', '\n')
