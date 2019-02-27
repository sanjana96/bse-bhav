import cherrypy
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('.'))


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('jinja_table_template.html')
        return tmpl.render(table=[['a', 'b', 'c'], ['d', 'e', 'f']])


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)

# cherrypy.quickstart(HelloWorld(), '/')