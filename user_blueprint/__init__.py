from flask import Blueprint

# 定义蓝图
users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

from . import routes