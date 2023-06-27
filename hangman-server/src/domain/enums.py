from enum import Enum


class GameStateEnum(Enum):
    IN_PROGRESS = 0
    WON = 1
    LOST = 2

    def to_enum_string(self):
        strings = {
            GameStateEnum.IN_PROGRESS: "IN_PROGRESS",
            GameStateEnum.WON: "WON",
            GameStateEnum.LOST: "LOST",
        }

        return strings[self]


class GuessResultEnum(Enum):
    CORRECT = 0
    INCORRECT = 1
    FAIL_INVALID_INPUT = 2
    FAIL_ALREADY_GAME_OVER = 3
    FAIL_ALREADY_GUESSED = 4

    def to_enum_string(self):
        strings = {
            GuessResultEnum.CORRECT: "CORRECT",
            GuessResultEnum.INCORRECT: "INCORRECT",
            GuessResultEnum.FAIL_INVALID_INPUT: "FAIL INVALID INPUT",
            GuessResultEnum.FAIL_ALREADY_GAME_OVER: "FAIL ALREADY GAME OVER",
            GuessResultEnum.FAIL_ALREADY_GUESSED: "FAIL ALREADY GUESSED",
        }

        return strings[self]


class HangmanGameScorerEnum(Enum):
    POINTS_PER_LETTER = 20
    POINTS_PER_REMAINING_GUESS = 10
