import cherrypy
from jinja2 import Environment, FileSystemLoader
import os
import csv

env = Environment(loader=FileSystemLoader('templates'))


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('jinja_table_template.html')
        csv_path = "EQ220219.CSV"
        table = []
        with open(csv_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                table.append(row)
        # TODO: Take this as argument in template
        # for index, col in enumerate(table[0]):
        #     if col == 'SC_NAME':
        #         name_col = index
        return tmpl.render(table=table)


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)


# cherrypy.quickstart(HelloWorld(), '/')