from secrets import choice
from injector import inject

from src.domain.enums import GameStateEnum
from src.domain.game_repository import GameRepository
from src.domain.game import HangmanGame
from src.infrastructure.config import config


class GameService:
    @inject
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
        self.words = config.get_words()
        self.guess_limit = config.get_guess_limit()

    def create_game(self):
        game = self._create_hangman_game()
        game_id = self.game_repository.save(game)
        return game_id, game

    def get_game(self, game_id):
        return self.game_repository.find_by_id(game_id)

    def make_guess(self, game_id, guess):
        game = self.game_repository.find_by_id(game_id)
        if not game:
            return None

        result = game.guess(guess)
        self.game_repository.save(game)

        # todo: delete game if user won or lost to manage memory but frontend needs to integrate with this change
        # if game.state == GameStateEnum.WON or game.state == GameStateEnum.LOST:
        #     self.game_repository.delete(game_id)

        return {
            "gameId": game_id,
            "state": game.state.name,
            "revealedWord": game.revealed_word,
            "numFailedGuessesRemaining": game.num_failed_guesses_remaining,
            "score": game.score,
            "guess": guess,
            "guessResult": result.value,
            "error": result.to_enum_string(),
        }

    def _create_hangman_game(self, words=None, guess_limit=5):
        words = words if words else self.words
        guess_limit = guess_limit if guess_limit else self.guess_limit

        if len(words) <= 0:
            raise ValueError("words must have at least 1 word")

        if guess_limit <= 0:
            raise ValueError("guess_limit must be greater than 0")

        rand_word = choice(words)
        return HangmanGame(rand_word, guess_limit)
