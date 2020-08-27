from flask import Flask
from flask_desktop_ui import FlaskDesktopUI


app = Flask(__name__)


@app.route('/')
def hello():
    return '<html><head><title>Hello world!</title></head><body><a href="./world">Hello...</a></body></html>'


@app.route('/world')
def world():
    return '<html><head><title>Hello world!</title></head><body><a href="./">WORLD!</a></body></html>'


def main():
    desktop_app = FlaskDesktopUI(app)
    desktop_app.run()


if __name__ == '__main__':
    main()
