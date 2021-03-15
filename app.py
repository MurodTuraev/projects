from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    r=request.values
    uname=r.get('uname',None)
    email=r.get('email',None)
    pas=r.get('pass',None)
    fname=r.get('fname',None)
    lname=r.get('lname',None)
    user=Register(username=uname,email=email,password=pas,fname=fname,lname=lname)
    users=Register.query.all()
    # total=f'Username: {users.username}'
    db.session.add(user)
    db.session.commit()
    for i in users:
        total=f''' Succesfully registerid!!!</p>
        Username: {i.username}
        <p>Email: {i.email}</p>
        <p>Password: {i.password}</p>
        <p>First name: {i.fname}</p>
        <p>Last Name: {i.lname}'''
        return total
    
    
if __name__ == '__main__':
    app.run(debug=True)
