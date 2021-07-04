from flask import Blueprint
from flask import request
from flask import render_template




frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static')


""" Wrapper to prevent circular imports """
def models_write_posts():
    from models import Post
    posts = Post
    return posts


""" Wrapper to prevent circular imports """
def models_posts():
    from models import Post
    posts = Post.query.all()
    return posts

@frontend.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    sale = models_write_posts()(title=request.form["title"], body=request.form["body"])
    db_session().session.add(sale)
    db_session().session.commit()
    return render_template('form.html')

@frontend.route('/')
def index():
    return render_template('index.html', posts=models_posts())


""" Wrapper to prevent circular imports """
def db_session():
    from app import db
    return db