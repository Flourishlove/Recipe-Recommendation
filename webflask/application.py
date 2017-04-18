# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.mysql import MySQL

from settings import APP_STATIC

application = Flask(__name__)
application.debug = True

mysql = MySQL()
"""
application.config['MYSQL_DATABASE_USER'] = 'root'
application.config['MYSQL_DATABASE_PASSWORD'] = 'FriApr14'
application.config['MYSQL_DATABASE_DB'] = 'recipe'
application.config['MYSQL_DATABASE_HOST'] = 'localhost'
"""
application.config['MYSQL_DATABASE_USER'] = 'flourishlove'
application.config['MYSQL_DATABASE_PASSWORD'] = 'MonApr17'
application.config['MYSQL_DATABASE_DB'] = 'recipe'
application.config['MYSQL_DATABASE_HOST'] = 'reciperecommendation.cky4qlh0i2dz.us-east-1.rds.amazonaws.com'
#application.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(application)
conn = mysql.connect()
cur = conn.cursor()

@application.route('/show')
def show_recipes():
    cur_flavor = request.args.get('flavor')
    print cur_flavor
    #cur.execute("SELECT name FROM recipes WHERE flavor = %s;", [cur_flavor])
    cur.execute("SELECT name FROM recipe_small WHERE dbscan_label = 3;")
    entries = cur.fetchall()
    return render_template('content.html', entries=entries)

@application.route('/', methods=['GET', 'POST'])
def choose_flavor():
    if request.method == 'POST':
        flavor = request.form['flavor']
        return redirect(url_for('show_recipes'), flavor=flavor)
    else:
        return render_template('index.html')


application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
