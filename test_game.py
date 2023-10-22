import pytest
from game import Game

# Sample data for learning modules
sample_learning_modules = ["Module 1", "Module 2", "Module 3"]

@pytest.fixture
def sample_game():
    return Game("Sample Game", sample_learning_modules)

def test_choose_game_difficulty_easy(sample_game, capsys, monkeypatch):
    # Simulate user input '1' for Easy
    monkeypatch.setattr('builtins.input', lambda _: '1')
    sample_game.choose_game_difficulty()
    captured = capsys.readouterr()
    assert "You have chosen Easy" in captured.out

def test_choose_game_difficulty_medium(sample_game, capsys, monkeypatch):
    # Simulate user input '1' for Easy
    monkeypatch.setattr('builtins.input', lambda _: '2')
    sample_game.choose_game_difficulty()
    captured = capsys.readouterr()
    assert "You have chosen Medium" in captured.out

def test_choose_game_difficulty_hard(sample_game, capsys, monkeypatch):
    # Simulate user input '1' for Easy
    monkeypatch.setattr('builtins.input', lambda _: '3')
    sample_game.choose_game_difficulty()
    captured = capsys.readouterr()
    assert "You have chosen Hard" in captured.out

def test_choose_lm(sample_game, capsys, monkeypatch):
    # Simulate user input '2' for Module 2
    monkeypatch.setattr('builtins.input', lambda _: '2')
    result = sample_game.choose_lm()
    assert result == "Module 2"

def test_play_game(capsys):
    sample_game = Game("Sample Game", sample_learning_modules)
    sample_game.play_game()
    captured = capsys.readouterr()
    assert "Coming soon!" in captured.out

def test_pause_game(capsys):
    sample_game = Game("Sample Game", sample_learning_modules)
    sample_game.pause_game()
    captured = capsys.readouterr()
    assert "Pause game..." in captured.out

# Negative testing
# def test_choose_game_difficulty_invalid_input(sample_game, capsys, monkeypatch):
#     # Simulate user input '4' which is invalid
#     monkeypatch.setattr('builtins.input', lambda _: '4')
#     with pytest.raises(SystemExit):
#         sample_game.choose_game_difficulty()
#     captured = capsys.readouterr()
#     assert "Please choose either Easy, Medium or Hard" in captured.out
#
# def test_choose_learning_module_invalid_input(sample_game, capsys, monkeypatch):
#     # Simulate user input '4' which is invalid
#     monkeypatch.setattr('builtins.input', lambda _: '4')
#     result = sample_game.choose_lm()
#     assert "Invalid Input!" in result

if __name__ == '__main__':
    pytest.main()
