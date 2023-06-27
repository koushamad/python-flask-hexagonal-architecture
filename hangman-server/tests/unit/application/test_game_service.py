import pytest
from unittest.mock import Mock

from src.application.game_service import GameService
from src.domain.game import HangmanGame
from src.domain.game_repository import GameRepository


# Creating a fixture for GameService
@pytest.fixture
def game_service():
    game_repository = Mock(spec=GameRepository)
    game_service = GameService(game_repository)
    return game_service


# Creating a fixture for HangmanGame
@pytest.fixture
def hangman_game():
    return HangmanGame("word", 5)


# Tests for GameService
def test_create_game(game_service):
    game_service.game_repository.save.return_value = 1
    game_id, game = game_service.create_game()
    assert isinstance(game_id, int)
    assert isinstance(game, HangmanGame)


def test_get_game(game_service, hangman_game):
    game_service.game_repository.find_by_id.return_value = hangman_game
    result = game_service.get_game(1)
    assert result == hangman_game


def test_make_guess(game_service, hangman_game):
    game_service.game_repository.find_by_id.return_value = hangman_game
    result = game_service.make_guess(1, "w")
    assert result["gameId"] == 1
    assert result["guess"] == "w"
