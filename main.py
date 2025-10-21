from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user/home.html')


@app.route('/pages')
def pages():
    return render_template('user/pages.html')


@app.route('/portafolio')
def portafolio():
    return render_template('user/portafolio.html')


@app.route('/blog')
def blog():
    return render_template('user/blog.html')


@app.route('/contact')
def contact():
    return render_template('user/contact.html')




if __name__ == '__main__':
    app.run(debug=True)