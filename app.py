import cherrypy
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime, timedelta
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import pandas as pd

env = Environment(loader=FileSystemLoader('templates'))


class HelloWorld(object):
    @cherrypy.expose
    def create_table(self, date):
        tmpl = env.get_template('jinja_table_template.html')
        year, month, day = date.split('-')
        year = year[-2:]
        csv_path = "EQ{}{}{}.CSV".format(day, month, year)
        resp = urlopen("https://www.bseindia.com/download/BhavCopy/Equity/{}_CSV.ZIP".format(csv_path.split('.')[0]))
        zipfile = ZipFile(BytesIO(resp.read()))
        df = pd.read_csv(zipfile.open(csv_path))
        table = df.values.tolist()
        return tmpl.render(heading='', table=table)

    @cherrypy.expose
    def index(self):
        yesterday_date = str(datetime.utcnow() - timedelta(1)).split()[0]
        return self.create_table(yesterday_date)
        # TODO: Take column number of name as argument in template
        # TODO: Pass header, make it pretty
        # return tmpl.render(heading='', table=table)


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)


# cherrypy.quickstart(HelloWorld(), '/')
