# flask-desktop-ui
Desktop web user interface using Flask APP as backend.

## Install
```shell
pip install flask-desktop-ui
```

## Usage
```python
from flask import Flask
from flask_desktop_ui import FlaskDesktopUI


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


def main():
    desktop_app = FlaskDesktopUI(app)
    desktop_app.run()


if __name__ == '__main__':
    main()
```

You can find more examples in `examples` folder
