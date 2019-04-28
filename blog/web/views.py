from flask import Blueprint, render_template

# from back.models import Article

web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/index/', methods=['GET'])
def index():
    # articles = Article.query.limit(14).all()
    return render_template('web/index.html')


@web_blueprint.route('/about/', methods=['GET'])
def about():
    return render_template('web/about.html')


@web_blueprint.route('/info/', methods=['GET'])
def info():
    return render_template('web/info.html')


@web_blueprint.route('/a_list/', methods=['GET'])
def a_list():
    return render_template('web/list.html')








