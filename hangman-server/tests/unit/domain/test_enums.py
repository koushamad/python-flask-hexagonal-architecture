from src.domain import enums


def test_game_state_enum_to_string():
    assert enums.GameStateEnum.IN_PROGRESS.to_enum_string() == "IN_PROGRESS"
    assert enums.GameStateEnum.WON.to_enum_string() == "WON"
    assert enums.GameStateEnum.LOST.to_enum_string() == "LOST"


def test_guess_result_enum_to_string():
    assert enums.GuessResultEnum.CORRECT.to_enum_string() == "CORRECT"
    assert enums.GuessResultEnum.INCORRECT.to_enum_string() == "INCORRECT"
    assert (
        enums.GuessResultEnum.FAIL_INVALID_INPUT.to_enum_string()
        == "FAIL INVALID INPUT"
    )
    assert (
        enums.GuessResultEnum.FAIL_ALREADY_GAME_OVER.to_enum_string()
        == "FAIL ALREADY GAME OVER"
    )
    assert (
        enums.GuessResultEnum.FAIL_ALREADY_GUESSED.to_enum_string()
        == "FAIL ALREADY GUESSED"
    )
