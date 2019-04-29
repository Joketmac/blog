from flask import Blueprint, render_template, url_for

from back.models import Article, ArticleType

web_blueprint = Blueprint('web', __name__)



@web_blueprint.route('/')
def index1():
    return 'hello'

@web_blueprint.route('/base_page/')
def base_page():
    return render_template('/web/base.html')

@web_blueprint.route('/about/')
def about1():
    return render_template('/web/about.html')

@web_blueprint.route('/gbook/')
def gbook():
    return render_template('/web/gbook.html')

@web_blueprint.route('/index/',methods=['GET'])
def index():
    articles = Article.query.all()
    categorys = ArticleType.query.all()
    return render_template('/web/index.html',articles=articles,categorys=categorys)

@web_blueprint.route('/info/')
def about():
    return render_template('/web/info.html')

@web_blueprint.route('/infopic/')
def infopic():
    return render_template('/web/infopic.html')

@web_blueprint.route('/list/')
def list():
    return render_template('/web/list.html')

@web_blueprint.route('/share/')
def share():
    return render_template('/web/share.html')








