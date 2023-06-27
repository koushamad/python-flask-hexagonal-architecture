from src.infrastructure.in_memory_game_repository import InMemoryGameRepository
from src.domain.game import HangmanGame


def test_in_memory_game_repository():
    game_repo = InMemoryGameRepository()
    game = HangmanGame("test", 3)

    game_id = game_repo.save(game)
    assert game_id == 1
    assert game_repo.find_by_id(1) == game

    game_repo.delete(1)
    assert game_repo.find_by_id(1) is None
