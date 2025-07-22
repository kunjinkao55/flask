from flask import render_template, request, redirect, url_for, session, flash
from . import users # 导入蓝图实例
from .extensions import db
from .models import User # 导入模型

#信息传递 POST(secreted) GET(unsecreted)
@users.route("/user",methods=['POST','GET'])
def user():
    email = None
    if "user" in session:
        usr = session["user"]
        if request.method == "POST":
            email = request.form["email"]#抓取email数据
            session["email"] = email#把email字段保存到session中
            found_user =User.query.filter_by(name = usr).first()
            found_user.email = email
            db.session.commit()

            flash(f"Saved Successfully, your email is {email}")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email = email)
    else:
        return render_template("login.html")

@users.route('/')
def home():
    return render_template("index.html")

@users.route("/view", methods=["POST","GET"])
def view():
    return render_template("view.html", values = User.query.all())

@users.route('/<name>/<int:times>')
def hello_world(name,times):
    #渲染html模板文件，templates里面
    return render_template("ts0.html",name = name,times = times)
# 重定向
@users.route('/re/<name>')
def re(name):
    return redirect(url_for("users.hello_world",name = name))

@users.route("/index")
def index():
    return render_template("index.html",name = "indexindex")

@users.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        user_id = request.form["_id"] # 获取隐藏字段传递的用户ID
        
        # 查找要删除的用户
        user_to_delete = User.query.get(user_id) # 或 User.query.filter_by(_id=user_id).first()
        
        if user_to_delete:
            db.session.delete(user_to_delete) # 从会话中删除对象
            db.session.commit() # 提交更改到数据库
            flash(f"用户 {user_to_delete.name} 已成功删除。", "success")
        else:
            flash("未找到要删除的用户。", "error")
            
    return redirect(url_for("users.view")) # 删除后重定向回用户列表页面

@users.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        #新登录
        session.permanent = True
        user = request.form["nm"]
        if user == "":
            return redirect(url_for("users.login"))
        email = None
        #使用数据库存储用户信息
        found_user =User.query.filter_by(name = user).first()
        #
        if found_user:
        # 找到了用户执行登录操作。
            # 将找到用户的 email 存储到会话中。
            session["email"] = found_user.email
            email = found_user.email
        else:
            # 如果未找到用户则执行自动注册操作。
            # 创建一个新的 users 对象实例，使用用户输入的用户名，
            # 并将 email 字段设置为空字符串。
            usr = User(user, "") 
            
            # 将新创建的 usr 对象添加到数据库会话中，准备将其保存到数据库。
            db.session.add(usr)
            db.session.commit()
#Sessions
#历时存储信息为全局变量的字典，实现在多个网页之间 快速访问，无需重复传
#路由参数就可以取消了
        session["user"] = user
        flash(f"login successfully!, your email is {email}")
        return redirect(url_for(".user"))
    else:
        if "user" in session:     #已经有登录数据
            flash("Already Logged in !")
            return redirect(url_for(".user"))

        else:
            return render_template("login.html")
#使用request.form.名字 获取html表单中的数据

@users.route("/logout",methods = ["POST"])
def logout():
    if "user" in session:
        user = session['user']
    session.pop("user",None)
    session.pop("email",None)
    flash(f"have been logged out,{user}", "info")
    return redirect(url_for("users.login"))
