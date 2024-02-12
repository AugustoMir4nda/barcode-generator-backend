from flask import Blueprint, request, jsonify
#Nomear rotas de tag com nomes específicos

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])

def create_tags():
    print(request.json)
    return jsonify({"resp": "ok"}), 200
