from src.domain.enums import GameStateEnum, HangmanGameScorerEnum, GuessResultEnum


class HangmanGame:
    def __init__(self, word=None, failed_guesses_limit=5):
        self._validate_input(word, failed_guesses_limit)

        self.score = 0
        self.word = word
        self.state = GameStateEnum.IN_PROGRESS
        self.guesses = []
        self.failed_guess_limit = failed_guesses_limit
        self.num_failed_guesses_remaining = failed_guesses_limit
        self.revealed_word = "_" * len(word)
        self.num_revealed_letters = 0

    def _validate_input(self, word, failed_guesses_limit):
        if failed_guesses_limit <= 0:
            self.state = GameStateEnum.LOST
            raise ValueError("failed_guesses_limit must be over 0")

        if len(word) <= 0:
            raise ValueError("word must have at least 1 letter")

    def guess(self, input_letter):
        if len(input_letter) != 1:
            return GuessResultEnum.FAIL_INVALID_INPUT
        elif input_letter in self.guesses:
            return GuessResultEnum.FAIL_ALREADY_GUESSED
        elif self.state != GameStateEnum.IN_PROGRESS:
            return GuessResultEnum.FAIL_ALREADY_GAME_OVER

        self.guesses.append(input_letter)

        if input_letter in self.word:
            self._handle_correct_guess(input_letter)
            return GuessResultEnum.CORRECT
        else:
            self._handle_incorrect_guess()
            return GuessResultEnum.INCORRECT

    def _handle_correct_guess(self, input_letter):
        self.revealed_word = "".join(
            [c if c in self.guesses else "_" for c in self.word]
        )
        self.num_revealed_letters = self.word.count(input_letter)
        self.score += (
            self.num_revealed_letters * HangmanGameScorerEnum.POINTS_PER_LETTER.value
        )
        if "_" not in self.revealed_word:
            self.state = GameStateEnum.WON

    def _handle_incorrect_guess(self):
        self.num_failed_guesses_remaining -= 1
        if self.num_failed_guesses_remaining == 0:
            self.state = GameStateEnum.LOST
