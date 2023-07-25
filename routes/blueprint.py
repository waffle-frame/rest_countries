from flask import Blueprint
from controllers.country import get


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/country', methods=['GET'])(get)
