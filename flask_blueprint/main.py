from flask import Flask
from apps import user_bp, book_bp, news_bp

app=Flask(__name__)
app.register_blueprint(user_bp) 
app.register_blueprint(book_bp) 
app.register_blueprint(news_bp) 
 

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    app.run(port=100,debug=True)