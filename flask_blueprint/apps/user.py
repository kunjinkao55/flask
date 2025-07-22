from . import user_bp
@user_bp.route('/list')
def user_list():
    return 'user_list'

@user_bp.route('/add')
def user_add():
    return 'user_add'
