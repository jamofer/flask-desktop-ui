import socket
from threading import Thread

from flask_desktop_ui import chromium_browser_wrapper

LOCAL_HOST = '127.0.0.1'
RANDOM_PORT = 0


class FlaskDesktopUI(object):
    def __init__(self, app):
        self.port = _get_random_port()
        self.flask_job = Thread(target=app.run, args=(LOCAL_HOST, self.port))
        self.flask_job.daemon = True

    def run(self):
        self.flask_job.start()
        chromium_browser_wrapper.initialize()
        chromium_browser_wrapper.open_url('http://{ip}:{port}'.format(ip=LOCAL_HOST, port=self.port))
        chromium_browser_wrapper.message_loop()


def _get_random_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((LOCAL_HOST, RANDOM_PORT))
    port = sock.getsockname()[1]
    sock.close()

    return port
