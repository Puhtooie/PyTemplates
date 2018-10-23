#azure cloud sql connection
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

app = fl(__name__)

params = urllib.parse.quote_plus('uri provided by azure')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()

#AWS Mysql connection
from flask import Flask as fl
from flask_sqlalchemy import SQLAlchemy as sa
app = fl(__name__)


application.config['SQLALCHEMY_DATABASE_URI'] = 'uri provided by aws'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    application.run()


#local sql connection
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

app = fl(__name__)

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=local_server_name;DATABASE=tempdb;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)

db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()

#local mysql connection

import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc
import pymysql

pymysql.install_as_MySQLdb()

app = fl(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Password@localhost/data_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()


