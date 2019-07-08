def wsgi_app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/plain")])
	return environ

bind = '0.0.0.0:8080'

