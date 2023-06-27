from typing import Optional
from src.domain.game_repository import GameRepository
from src.domain.game import HangmanGame


class InMemoryGameRepository(GameRepository):
    def __init__(self):
        self.games = {}
        self.next_game_id = 1

    def save(self, game: HangmanGame) -> int:
        game_id = self.next_game_id
        self.games[game_id] = game
        self.next_game_id += 1
        return game_id

    def find_by_id(self, game_id: int) -> Optional[HangmanGame]:
        return self.games.get(game_id, None)

    def delete(self, game_id: int) -> None:
        del self.games[game_id]
