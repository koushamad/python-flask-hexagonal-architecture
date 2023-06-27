from src.domain import game, enums


def test_guess_correct():
    hangman_game = game.HangmanGame("word", 5)
    result = hangman_game.guess("w")
    assert result == enums.GuessResultEnum.CORRECT
    assert hangman_game.state == enums.GameStateEnum.IN_PROGRESS
    assert hangman_game.revealed_word == "w___"


def test_guess_incorrect():
    hangman_game = game.HangmanGame("word", 5)
    result = hangman_game.guess("a")
    assert result == enums.GuessResultEnum.INCORRECT
    assert hangman_game.state == enums.GameStateEnum.IN_PROGRESS
    assert hangman_game.revealed_word == "____"


def test_guess_invalid_input():
    hangman_game = game.HangmanGame("word", 5)
    result = hangman_game.guess("wa")
    assert result == enums.GuessResultEnum.FAIL_INVALID_INPUT


def test_guess_game_over():
    hangman_game = game.HangmanGame("word", 5)
    hangman_game.state = enums.GameStateEnum.WON
    result = hangman_game.guess("w")
    assert result == enums.GuessResultEnum.FAIL_ALREADY_GAME_OVER


def test_guess_already_guessed():
    hangman_game = game.HangmanGame("word", 5)
    hangman_game.guess("w")
    result = hangman_game.guess("w")
    assert result == enums.GuessResultEnum.FAIL_ALREADY_GUESSED
