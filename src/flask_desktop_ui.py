from threading import Thread

import chromium_browser


LOCAL_HOST = '127.0.0.1'
FLASK_PORT = 62191


class FlaskDesktopUI(object):
    def __init__(self, app):
        self.flask_job = Thread(target=app.run, args=(LOCAL_HOST, FLASK_PORT))
        self.flask_job.daemon = True

    def run(self):
        self.flask_job.start()
        chromium_browser.initialize()
        chromium_browser.open_url('http://{ip}:{port}'.format(ip=LOCAL_HOST, port=FLASK_PORT))
        chromium_browser.message_loop()


def default_page():
    return 'Define a rule for "/" in your flask APP'
