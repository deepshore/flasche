import os

from .settings import FLASCHE_APP_FILE as APP_FILE


KEY = 'FLASK_APP'


class ProjectRunner:
    def __init__(self, project):
        self.project = project

    def run_flask_app(self, flask_app):
        os.environ[KEY] = flask_app
        os.system('flask run')

    def run(self):
        _flask_app = os.getenv(KEY)
        flask_app = os.path.join(self.project, APP_FILE)
        try:
            self.run_flask_app(flask_app)
        finally:
            if _flask_app:
                os.environ[KEY] = _flask_app
            else:
                del os.environ[KEY]
