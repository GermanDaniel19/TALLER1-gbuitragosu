from models.cuidador import Cuidador
from flask import jsonify, Blueprint

cuidador_blueprint = Blueprint('cuidador_bp', __name__, url_prefix="/users")

@cuidador_blueprint.route('/')
def index():
    guarderia = Cuidador.query.all()
    return jsonify({"data": guarderia[0].nombre}), 201