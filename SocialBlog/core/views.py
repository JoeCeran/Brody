# core/views.py

from flask import render_template,request,Blueprint
from SocialBlog.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # MORE TO COME!
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/about')
def about():
    return render_template('About.html')

@core.route('/signin')
def signin():
    # MORE TO COME!
    return render_template('Signin.html')
