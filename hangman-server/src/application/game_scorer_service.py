from src.domain.enums import HangmanGameScorerEnum


class HangmanGameScorer:
    @classmethod
    def score(cls, game):
        points = (
            game.num_revealed_letters * HangmanGameScorerEnum.POINTS_PER_LETTER.value
        )
        points += (
            game.num_failed_guesses_remaining
            * HangmanGameScorerEnum.POINTS_PER_REMAINING_GUESS.value
        )
        return points
