from . import news_bp
@news_bp.route('/list')
def news_list():
    return 'news_list'

@news_bp.route('/add')
def news_add():
    return 'news_add'
