from abc import ABC, abstractmethod
from typing import Optional
from src.domain.game import HangmanGame


class GameRepository(ABC):
    @abstractmethod
    def save(self, game: HangmanGame) -> int:
        pass

    @abstractmethod
    def find_by_id(self, game_id: int) -> Optional[HangmanGame]:
        pass

    @abstractmethod
    def delete(self, game_id: int) -> None:
        pass
