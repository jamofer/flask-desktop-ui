import os

from flask import Flask, render_template
from flask_desktop_ui import FlaskDesktopUI


app = Flask(__name__)


@app.route('/')
def os_info():
    return render_template('os_info.html', uname=os.uname())


def main():
    desktop_app = FlaskDesktopUI(app)
    desktop_app.run()


if __name__ == '__main__':
    main()
