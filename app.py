from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Register(db.Model):
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))


@app.route('/')
def home():
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
