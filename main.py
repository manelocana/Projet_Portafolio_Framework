from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user/home.html')


@app.route('/pages')
def pages():
    return render_template('user/pages.html')


@app.route('/portfolio')
def portafolio():
    return render_template('user/portfolio.html')


@app.route('/blog')
def blog():
    return render_template('user/blog.html')


@app.route('/contact')
def contact():
    return render_template('user/contact.html')


@app.route('/admin')
def admin_home():
    return render_template('admin/home.html')


@app.route('/admin/portfolio')
def admin_portfolio():
    return render_template('admin/portfolio.html')


@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')






if __name__ == '__main__':
    app.run(debug=True)