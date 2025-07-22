from flask import Blueprint
book_bp = Blueprint('book',__name__,url_prefix='/book')
news_bp = Blueprint('news',__name__,url_prefix='/news')
user_bp = Blueprint('user',__name__,url_prefix='/user')

from . import book,news,user