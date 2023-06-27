import json
import pytest
from unittest.mock import MagicMock
from src.server import app
from src.domain.game import HangmanGame

mock_create_hangman_game1 = MagicMock(return_value=HangmanGame("test", 5))
mock_create_hangman_game2 = MagicMock(return_value=HangmanGame("test", 2))


def parse_response(response):
    return json.loads(response.get_data().decode())


def post_guess(client, game_id, letter):
    response = client.post(f"/api/hangman/{game_id}/guess", json={"letter": letter})
    return parse_response(response)


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def game1(monkeypatch, client):
    monkeypatch.setattr(
        "src.application.game_service.GameService._create_hangman_game",
        mock_create_hangman_game1,
    )
    response = client.post("/api/hangman")
    return parse_response(response)


@pytest.fixture
def game2(monkeypatch, client):
    monkeypatch.setattr(
        "src.application.game_service.GameService._create_hangman_game",
        mock_create_hangman_game2,
    )
    response = client.post("/api/hangman")
    return parse_response(response)


@pytest.fixture
def game_get_resource(client, game1):
    game_id = game1["gameId"]
    response = client.get(f"/api/hangman/{game_id}")
    return parse_response(response)


def validate_response_data(
    response_data, state, revealed_word, num_failed_guesses_remaining, score, error
):
    assert "gameId" in response_data, "Missing 'gameId' in response data"
    assert (
        response_data["state"] == state
    ), f"Expected state '{state}', got '{response_data['state']}'"
    assert (
        response_data["revealedWord"] == revealed_word
    ), f"Expected revealedWord '{revealed_word}', got '{response_data['revealedWord']}'"
    assert (
        response_data["numFailedGuessesRemaining"] == num_failed_guesses_remaining
    ), f"Expected numFailedGuessesRemaining '{num_failed_guesses_remaining}', got '{response_data['numFailedGuessesRemaining']}'"
    assert (
        response_data["score"] == score
    ), f"Expected score '{score}', got '{response_data['score']}'"
    assert (
        response_data.get("error") == error
    ), f"Expected error '{error}', got '{response_data.get('error')}'"


def test_create_game(game1):
    validate_response_data(game1, "IN_PROGRESS", "____", 5, 5 * 10, None)
    mock_create_hangman_game1.assert_called_once()


def test_get_game(game_get_resource):
    validate_response_data(game_get_resource, "IN_PROGRESS", "____", 5, 5 * 10, None)


def test_guess_won_already_guessed(client, game1):
    game_id = game1["gameId"]
    response_data = post_guess(client, game_id, "t")
    validate_response_data(response_data, "IN_PROGRESS", "t__t", 5, 4 * 10, "CORRECT")

    response_data = post_guess(client, game_id, "t")
    validate_response_data(
        response_data, "IN_PROGRESS", "t__t", 5, 4 * 10, "FAIL ALREADY GUESSED"
    )


def test_guess_won_invalid(client, game1):
    game_id = game1["gameId"]
    response_data = post_guess(client, game_id, "tt")
    validate_response_data(
        response_data, "IN_PROGRESS", "t__t", 5, 40, "FAIL INVALID INPUT"
    )


def test_guess_won_incorrect(client, game1):
    game_id = game1["gameId"]
    response_data = post_guess(client, game_id, "p")
    validate_response_data(response_data, "IN_PROGRESS", "t__t", 4, 40, "INCORRECT")


def test_guess_won_correct(client, game1):
    game_id = game1["gameId"]
    response_data = post_guess(client, game_id, "s")
    validate_response_data(response_data, "IN_PROGRESS", "t_st", 4, 6 * 10, "CORRECT")

    response_data = post_guess(client, game_id, "e")
    validate_response_data(response_data, "WON", "test", 4, 8 * 10, "CORRECT")


def test_guess_won(client, game1):
    game_id = game1["gameId"]
    response_data = post_guess(client, game_id, "p")
    validate_response_data(response_data, "WON", "test", 4, 80, "FAIL ALREADY GUESSED")


def test_guess_lost_incorrect(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "p")
    validate_response_data(response_data, "IN_PROGRESS", "____", 1, 0, "INCORRECT")


def test_guess_lost_correct(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "e")
    validate_response_data(response_data, "IN_PROGRESS", "_e__", 1, 20, "CORRECT")


def test_guess_lost_invalid(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "e3")
    validate_response_data(
        response_data, "IN_PROGRESS", "_e__", 1, 20, "FAIL INVALID INPUT"
    )


def test_guess_lost_fail_already_guessed(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "e")
    validate_response_data(
        response_data, "IN_PROGRESS", "_e__", 1, 20, "FAIL ALREADY GUESSED"
    )


def test_guess_lost_fail(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "k")
    validate_response_data(response_data, "LOST", "_e__", 0, 20, "INCORRECT")


def test_guess_lost_fail_already_game_over(client, game2):
    game_id = game2["gameId"]
    response_data = post_guess(client, game_id, "l")
    validate_response_data(
        response_data, "LOST", "_e__", 0, 20, "FAIL ALREADY GAME OVER"
    )
