from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    @app.route("/")
    def index():
        return "Hello, Word"


    with app.app_context():
        return app