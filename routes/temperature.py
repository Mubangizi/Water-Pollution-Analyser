from flask import request, Blueprint
temperature_bp = Blueprint('temperature', __name__)

@temperature_bp.route('/get_temperatures/', methods=['GET'])
def get_temperatures():
    pass