from flask import Flask
from flask_cors import CORS
from routes.test import test
from routes.test_1 import test_1

def create_app():
    app = Flask(__name__)

    # Enable CORS for all routes with specified origins
    CORS(app)
    CORS(app, origins='*')

    # Register the blueprint with the Flask app
    app.register_blueprint(test)
    app.register_blueprint(test_1)

    # Example route for returning a plain text response
    @app.route('/')
    def hello():
        app.logger.info('Hello route triggered')
        return f'Hello from the Digital Signature Service API v{test.version}'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host="0.0.0.0", port=6002)