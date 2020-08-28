from threading import Thread

from flask_desktop_ui import chromium_browser_wrapper

LOCAL_HOST = '127.0.0.1'
FLASK_PORT = 62191


class FlaskDesktopUI(object):
    def __init__(self, app):
        self.flask_job = Thread(target=app.run, args=(LOCAL_HOST, FLASK_PORT))
        self.flask_job.daemon = True

    def run(self):
        self.flask_job.start()
        chromium_browser_wrapper.initialize()
        chromium_browser_wrapper.open_url('http://{ip}:{port}'.format(ip=LOCAL_HOST, port=FLASK_PORT))
        chromium_browser_wrapper.message_loop()
