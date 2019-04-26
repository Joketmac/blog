from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from back.models import User, Article, ArticleType,  db
from utils.functions import is_login

back_blueprint = Blueprint('back', __name__)



@back_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('back/register.html')
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if username and password and password2:

            user = User.query.filter(User.username == username).first()
            if user:
                error = '该账号已注册, 请更换账号'
                return render_template('back/register.html', error=error)
            else:
                if password2 == password:

                    user = User()
                    user.username = username
                    user.password = generate_password_hash(password)
                    user.save()
                    return redirect(url_for('back.login'))

                else:

                    error = '两次密码不一致'
                    return render_template('back/register.html', error=error)
        else:
            error = '请填写完整信息'
            return render_template('back/register.html', error=error)


@back_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('back/login.html')

    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter(User.username == username).first()
            if not user:
                error = '该账号不存在, 请前往注册'
                return render_template('back/login.html', error=error)
            if not check_password_hash(user.password, password):
                error = '密码错误, 请修改密码'
                return render_template('back/login.html', error=error)
            session['user_id'] = user.id
            return redirect(url_for('back.index'))
        else:
            error = '请填写完整的登录信息'
            return render_template('back/login.html', error=error)


@back_blueprint.route('/index/', methods=['GET'])
@is_login
def index():
    # 获取session，通过id 拿到用户名  渲染到前端页面
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    username = user.username  # bug:如果没有注册过这里会报错
    return render_template('back/index.html', username=username)


@back_blueprint.route('/logout/', methods=['GET'])
@is_login
def logout():
    del session['user_id']
    return redirect(url_for('back.login'))


@back_blueprint.route('/a_type/', methods=['GET', 'POST'])
def a_type():
    if request.method == 'GET':
        types = ArticleType.query.all()
        return render_template('back/category.html', types=types)


@back_blueprint.route('/add_category/', methods=['GET', 'POST'])
def add_type():
    if request.method == 'GET':
        return render_template('back/add-category.html')
    if request.method == 'POST':
        atype = request.form.get('atype')
        if atype:
            art_type = ArticleType()
            art_type.t_name = atype
            db.session.add(art_type)
            db.session.commit()
            return redirect(url_for('back.a_type'))
        else:
            error = '请填写分类信息'
            return render_template('back/add-category.html')


@back_blueprint.route('/del_type/<int:id>/', methods=['GET', 'POST'])
def del_type(id):
    atype = ArticleType.query.get(id)
    db.session.delete(atype)
    db.session.commit()
    return redirect(url_for('back.a_type'))


@back_blueprint.route('/article/', methods=['GET', 'POST'])
def article():
    if request.method == 'GET':
        articles = Article.query.all()
        return render_template('back/article.html', articles=articles)


@back_blueprint.route('/add_article/', methods=['GET', 'POST'])
def article_add():
    if request.method == 'GET':
        types = ArticleType.query.all()
        return render_template('back/add-article.html', types=types)
    if request.method == 'POST':
        print('james')
        title = request.form.get('title')
        desc = request.form.get('desc')
        category = request.form.get('category')
        content = request.form.get('content')
        if title and desc and category and content:

            art = Article()
            art.title = title
            art.desc = desc
            art.content = content
            art.type = category
            db.session.add(art)
            db.session.commit()
            return redirect(url_for('back.article'))
        else:
            error = '请填写完整的文章信息'

            return render_template('back/add-article.html', error=error)


@back_blueprint.route('/w_index', methods=['GET'])
def w_index():
    return render_template('web/index.html')
