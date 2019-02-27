import cherrypy
from jinja2 import Environment, FileSystemLoader
import os
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import pandas as pd

env = Environment(loader=FileSystemLoader('templates'))


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('jinja_table_template.html')
        resp = urlopen("https://www.bseindia.com/download/BhavCopy/Equity/EQ250219_CSV.ZIP")
        zipfile = ZipFile(BytesIO(resp.read()))
        csv_path = "EQ250219.CSV"
        df = pd.read_csv(zipfile.open(csv_path))
        table = df.values.tolist()
        # TODO: Take column number of name as argument in template
        # TODO: Pass header, make it pretty
        # TODO: Block all future dates
        return tmpl.render(heading='', table=table)


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

# cherrypy.quickstart(HelloWorld(), '/', config=config)


cherrypy.quickstart(HelloWorld(), '/')