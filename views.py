from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

app_bp = Blueprint('main', __name__)

@app_bp.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)

    except ValidationError as e:
        return e.message, 404

    result = None
    for query in params['queries']:
        result = build_query(cmd=query['cmd'], param=query['param'], data=result)

    return jsonify(result)


