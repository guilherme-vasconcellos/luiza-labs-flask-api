from flask import current_app as app, Blueprint

health_bp = Blueprint('health', __name__)


@health_bp.route('/', methods=['GET'])
def health_check():
    return '', 200
