from flask import Flask

from flask_cors import CORS
from flask_compress import Compress
from flask_talisman import Talisman

from app.models.base import db, ma
from app.models.employee import Employee

from app.routes.health import health_bp
from app.routes.employee import employee_bp


def create_app(config_file):
    """
    @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
    @description: App factory function to get a configured app instance
    """
    app = Flask(__name__)

    # App config
    app.url_map.strict_slashes = False
    app.config.from_pyfile(config_file)

    # Middlewares setup
    CORS(app)
    Compress(app)
    Talisman(app)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Routes registration
    app.register_blueprint(health_bp, url_prefix='/health')
    app.register_blueprint(employee_bp, url_prefix='/employee')

    # Create tables on database
    with app.app_context():
        db.create_all()

    return app


def main():
    """
    @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
    @description: Start server instance
    """
    app = create_app('app/config.py')
    app.run()


if __name__ == '__main__':
    main()
