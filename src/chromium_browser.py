import sys

from cefpython3 import cefpython


def initialize():
    sys.excepthook = cefpython.ExceptHook
    cefpython.Initialize()


def open_url(url):
    cefpython.CreateBrowserSync(url=url)


def message_loop():
    cefpython.MessageLoop()
    cefpython.Shutdown()
