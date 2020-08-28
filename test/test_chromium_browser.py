import sys
import unittest

from cefpython3 import cefpython
from mock import patch, Mock, call

from flask_desktop_ui import chromium_browser_wrapper


class TestChromiumBrowser(unittest.TestCase):
    def setUp(self):
        self.Initialize = patch('cefpython3.cefpython.Initialize').start()
        self.CreateBrowserSync = patch('cefpython3.cefpython.CreateBrowserSync').start()
        self.MessageLoop = patch('cefpython3.cefpython.MessageLoop').start()
        self.Shutdown = patch('cefpython3.cefpython.Shutdown').start()

    def tearDown(self):
        patch.stopall()

    def test_it_initializes_chromium_browser(self):
        chromium_browser_wrapper.initialize()

        self.Initialize.assert_called_once()
        assert sys.excepthook == cefpython.ExceptHook

    def test_it_opens_a_url(self):
        chromium_browser_wrapper.open_url('http://xd.com')

        self.CreateBrowserSync.assert_called_once_with(url='http://xd.com')

    def test_it_runs_chromium_browser_message_loop(self):
        chromium_browser_wrapper.message_loop()

        self.MessageLoop.assert_called_once()

    def test_it_shutdowns_cefpython_when_message_loop_ends(self):
        cefpython = Mock()
        cefpython.attach_mock(self.MessageLoop, 'MessageLoop')
        cefpython.attach_mock(self.Shutdown, 'Shutdown')

        chromium_browser_wrapper.message_loop()

        cefpython.assert_has_calls([
            call.MessageLoop(),
            call.Shutdown(),
        ])
