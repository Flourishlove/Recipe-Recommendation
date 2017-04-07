# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , recipe.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'recipe.db'),
    SECRET_KEY='Wed52017Apr',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('RECIPE_SETTINGS', silent=True)



def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv



def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



@app.route('/')
def show_labels():
    db = get_db()
    cur = db.execute('select flavor from recipes group by flavor')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)


@app.route('/choose', methods=['POST'])
def choose_flavor():
    if request.form['action'] == 'sweet':
        flavor = 'sweet'
    elif request.form['action'] == 'spicy':
        flavor = 'spicy'
    else:
        flavor = 'hot'
    flash('Choose flavor successfully')
    return redirect(url_for('show_recipes', flavor=flavor))

@app.route('/show')
def show_recipes():
    cur_flavor = request.args.get('flavor')
    print cur_flavor
    db = get_db()
    cur = db.execute('select name from recipes where flavor = (?)', (cur_flavor,))
    entries = cur.fetchall()
    return render_template('content.html', entries=entries)

