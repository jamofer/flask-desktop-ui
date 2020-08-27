import os
import random

from flask import Flask
from flask_desktop_ui import FlaskDesktopUI


STATIC_FARMER_FOLDER = os.path.dirname(__file__) + 'static_farmer'


app = Flask(__name__, static_url_path='', static_folder=STATIC_FARMER_FOLDER)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/search_wife')
def search_wife():
    return random.choice(['Antonia', 'Eusevia', 'Julia', 'Manuela', 'Consuelo'])


def main():
    desktop_app = FlaskDesktopUI(app)
    desktop_app.run()


if __name__ == '__main__':
    main()
