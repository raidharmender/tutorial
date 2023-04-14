from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html")


@app.route('/name')
def name():
    return "<html><body><h1>Hello</h1></body></html>"

@app.route('/news')
def news():
    return '<h2>Go to CNN.com<h2>'


if __name__ == '__main__':
    app.run()
