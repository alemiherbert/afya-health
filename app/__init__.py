from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from .main import main
        app.register_blueprint(main)
        return app
