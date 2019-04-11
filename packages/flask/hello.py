# -*- coding: utf-8 -*-

from flask import Flask,request,make_response,render_template
app = Flask(__name__)

@app.route('/')
def index():
    # 读取 cookies:
    username = request.cookies.get('username')
    # 使用 cookies.get(key) 来代替 cookies[key] ，
    # 以避免当 cookie 不存在时引发 KeyError 。

    # 储存 cookies
    resp = make_response(render_template(""))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print "post"
    else:
        print "get"


if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
