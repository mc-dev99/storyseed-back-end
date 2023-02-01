from flask import Blueprint, request, jsonify, make_response, abort
import os, requests

decks_bp = Blueprint("decks_bp", __name__, url_prefix="/decks")

# def validate_model(cls, model_id):
#     try:
#         model_id = int(model_id)
#     except:
#         abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

#     model = cls.query.get(model_id)

#     if not model:
#         abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

#     return model

### DECK ROUTES ###

# @boards_bp.route("", methods=["POST"])
# def create_board():
#     request_body = request.get_json()
#     new_board = Board.from_dict(request_body)
    
#     db.session.add(new_board)
#     db.session.commit()
    
#     return make_response(jsonify(new_board.to_dict()), 201)

@decks_bp.route("", methods=["GET"])
def hello_word():
    return jsonify({
            'greeting': 'Hello World!'
        })