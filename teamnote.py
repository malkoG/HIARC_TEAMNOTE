from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', defaults={'path': 'index.html'})
@app.route("/<path:path>")
def main_route(path):
        return  render_template('index.html')


if __name__ == '__main__':
    app.run()
