from flask import Flask, render_template, request, redirect


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


#request.files pour les images (no .form)
 #apres le post => redirect url
@app.route('/admin/portfolio/ajouter', methods=['POST'])
def admin_portfolio_ajouter():
    _name = request.form['txt_name']
    _file = request.files['txt_img']

    print(_name)
    print(_file)
    return redirect('/admin/portfolio')
    




if __name__ == '__main__':
    app.run(debug=True)