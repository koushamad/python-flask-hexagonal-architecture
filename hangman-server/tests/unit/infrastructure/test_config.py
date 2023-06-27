import os
from src.infrastructure import config


def test_config_load_and_save():
    config_instance = config.Config()
    config_instance.WORDS = ["test", "config"]
    config_instance.GUESS_LIMIT = 10
    config_instance.save_config()

    loaded_config = config.Config()
    loaded_config.load_config()

    assert loaded_config.WORDS == ["test", "config"]
    assert loaded_config.GUESS_LIMIT == 10

    # Cleaning up by removing the file
    os.remove(config_instance.config_file_path)
