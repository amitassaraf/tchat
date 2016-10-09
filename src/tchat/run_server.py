from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler

from tchat.app import app
from tchat.settings import PORT, IP
from tchat.ws_handler import AppWebSocketHandler


def run_server():
    flask_container = WSGIContainer(app)

    application = Application([
        # An simple handler for
        (r"/ws", AppWebSocketHandler),
        (r".*", FallbackHandler, dict(fallback=flask_container)),
    ], compress_response=True)

    application.listen(PORT, IP)

    IOLoop.instance().start()

if __name__ == '__main__':
    run_server()
