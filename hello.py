def wsgi_app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/plain")])
	res = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	return res

bind = '0.0.0.0:8080'

