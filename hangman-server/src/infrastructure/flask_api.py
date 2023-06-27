from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS
from injector import inject

from src.application.game_scorer_service import HangmanGameScorer
from src.domain.game import HangmanGame
from src.application.game_service import GameService

api = Blueprint("api", __name__)
CORS(api)


def hangman_game_to_dto(game_id: int, game: HangmanGame):
    return {
        "gameId": game_id,
        "state": game.state.to_enum_string(),
        "revealedWord": game.revealed_word,
        "numFailedGuessesRemaining": game.num_failed_guesses_remaining,
        "score": HangmanGameScorer.score(game),
    }


@inject
@api.route("/api/hangman", methods=["POST"])
def post_hangman(game_service: GameService):
    game_id, game = game_service.create_game()
    return jsonify(hangman_game_to_dto(game_id, game)), 200


@inject
@api.route("/api/hangman/<int:game_id>", methods=["GET"])
def get_hangman(game_id, game_service: GameService):
    game = game_service.get_game(game_id)

    if game is None:
        return make_response(jsonify({"error": "Game not found"}), 404)

    return jsonify(hangman_game_to_dto(game_id, game)), 200


@inject
@api.route("/api/hangman/<int:game_id>/guess", methods=["POST"])
def guess(game_id, game_service: GameService):
    if not request.json or "letter" not in request.json:
        return jsonify({"error": "Missing guess in request body"}), 400

    guess = request.json["letter"]
    result = game_service.make_guess(game_id, guess)
    if not result:
        return jsonify({"error": "Unable to process guess"}), 400

    return jsonify(result), 200
