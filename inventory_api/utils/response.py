from flask import jsonify
def api_response(data=None, message="Success", status=200):
    return jsonify({
        "message": message,
        "data": data
    }), status
