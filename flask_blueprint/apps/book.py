from . import book_bp
@book_bp.route('/')
def book():
    return 'book'

@book_bp.route('/list')
def book_list():
    return 'book_list'

@book_bp.route('/add')
def book_add():
    return 'book_add'
