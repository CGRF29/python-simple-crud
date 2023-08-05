from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/flask/")
def hello_flask():
    return "<p>Hello, Flask!</p>"


@app.route("/gaby")
def hello_gaby():
    return "<p>Hello, Gaby!</p>"

if __name__ == '__main__':
    app.run(debug = True)