import cherrypy
import os


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)