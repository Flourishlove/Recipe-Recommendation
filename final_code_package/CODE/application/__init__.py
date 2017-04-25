from flask import Flask

application = app = Flask(__name__)
app.config.from_object('config')