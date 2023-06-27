from src.application.game_scorer_service import HangmanGameScorer
from src.domain.enums import HangmanGameScorerEnum
import pytest
from src.domain.game import HangmanGame


@pytest.fixture
def hangman_game():
    return HangmanGame("word", 5)


def test_score(hangman_game):
    hangman_game.num_revealed_letters = 3
    hangman_game.num_failed_guesses_remaining = 2
    score = HangmanGameScorer.score(hangman_game)
    assert score == (3 * HangmanGameScorerEnum.POINTS_PER_LETTER.value) + (
        2 * HangmanGameScorerEnum.POINTS_PER_REMAINING_GUESS.value
    )
