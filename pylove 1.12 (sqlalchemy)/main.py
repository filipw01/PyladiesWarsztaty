from os import path
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import BlogPosts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.app = app
db.init_app(app)
lm = LoginManager()
lm.init_app(app)
bcrypt = Bcrypt()
app.static_path = path.join(path.abspath(__file__), 'static')


@app.route("/")
def main():
    blogposts = BlogPosts.query.all()
    return render_template("main.html", blogposts=blogposts)

if __name__ == '__main__':
    app.run(debug=True)