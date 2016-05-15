def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = env['QUERY_STRING']
    url = url.split('&')
    url2 = [x + '\n' for x in url]
    return url2
