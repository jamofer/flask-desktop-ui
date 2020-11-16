import socket
import unittest
from time import sleep

import pytest
from mock import patch, MagicMock

import flask_desktop_ui


class TestFlaskDesktopUI(unittest.TestCase):
    def setUp(self):
        self.initialize = patch('flask_desktop_ui.chromium_browser_wrapper.initialize').start()
        self.open_url = patch('flask_desktop_ui.chromium_browser_wrapper.open_url').start()
        self.message_loop = patch('flask_desktop_ui.chromium_browser_wrapper.message_loop').start()
        self.socket = patch('socket.socket').start()

    def tearDown(self):
        patch.stopall()

    def test_it_runs_flask_desktop_ui(self):
        sock = MagicMock()
        sock.getsockname.return_value = ('127.0.0.1', 10000)
        self.socket.return_value = sock
        app = MagicMock()
        desktop_app = flask_desktop_ui.FlaskDesktopUI(app)

        desktop_app.run()

        wait_until_called(app.run)
        app.run.assert_called_once_with(flask_desktop_ui.LOCAL_HOST, 10000)
        self.initialize.assert_called_once()
        self.socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind.assert_called_once_with((flask_desktop_ui.LOCAL_HOST, flask_desktop_ui.RANDOM_PORT))
        self.open_url.assert_called_once_with(
            'http://{ip}:{port}'.format(ip=flask_desktop_ui.LOCAL_HOST, port=10000)
        )
        self.message_loop.assert_called_once()


def wait_until_called(target_mock, timeout=1, attempt_delay=0.1):
    time = 0

    while time < timeout:
        if target_mock.called:
            return

        time += attempt_delay
        sleep(attempt_delay)

    pytest.fail('Timeout waiting for {} to be called after {} seconds'.format(target_mock, timeout))
