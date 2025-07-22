from flask import Flask, redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from user_blueprint.extensions import db, migrate # 从 extensions.py 导入 db 和 migrate
from user_blueprint import users # 导入蓝图实例
#闪烁信息条 flash 默认只记录最后一条消息

#数据库 SQL alchemy
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "password"#session需要密码
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'#要链接的数据库路径
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#禁用追踪提升性能
    app.permanent_session_lifetime = timedelta(days=3)

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图
    # url_prefix 参数可以为蓝图的所有路由添加一个前缀，例如 /users/login
    app.register_blueprint(users) 
  
    with app.app_context():
        db.create_all() # 在这里创建所有数据库表

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)