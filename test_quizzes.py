import pytest
from unittest.mock import patch
from quizzes import Quizzes


# Fixture for sample_quiz
quiz1_ans_easy = ["50", "3.0", "1"]
quiz1_ans_medium = ["d", "b", "b"]
quiz1_ans_hard = ["q", "60", "65"]
quiz1_easy_questions = ["(2 + 3) * (13 - 3) = ?", "2 ** 3 / 2 - 4 + 3", "5 // 9 + 3 % 2"]
quiz1_medium_questions = ["""Which operator is used for exponentiation in Python?\na) + \nb) * \nc) ^ \nd) ** \n""",
                          """Which of the following data types is used to store a single character in Python?\na) int\nb) str\nc) float\nd) bool\n""",
                          """What is the primary purpose of a Python function?\na) To store data\nb) To perform a specific task or operation\nc) To create a class\nd) To define a loop\n
                          """]

quiz1_hard_questions = ["To be IMPLEMENTED SOON. Please input 'q' to quit"]

sample_quiz = Quizzes(
    quiz1_ans_easy,
    quiz1_ans_medium,
    quiz1_ans_hard,
    quiz1_easy_questions,
    quiz1_medium_questions,
    quiz1_hard_questions
)

# Positive Testing
@patch('builtins.input', side_effect=['1'])
def test_choose_difficulty_easy(mock_input):
    result = sample_quiz.choose_difficulty()
    assert result == "Easy"

@patch('builtins.input', side_effect=['2'])
def test_choose_difficulty_medium(mock_input):
    result = sample_quiz.choose_difficulty()
    assert result == "Medium"

@patch('builtins.input', side_effect=['3'])
def test_choose_difficulty_hard(mock_input):
    result = sample_quiz.choose_difficulty()
    assert result == "Hard"

# Corrected test cases for validate_ans
def test_validate_ans_correct():
    quiz = Quizzes(quiz1_ans_easy, [], [], [], [], [])
    assert quiz.validate_ans("50", quiz1_ans_easy, 0) is True

# Negative testing
@patch('builtins.input', side_effect=['5', '1'])
def test_choose_difficulty_invalid_input(mock_input):
    result = sample_quiz.choose_difficulty()
    assert result == "Easy"

@patch('builtins.input', side_effect=['abc', '2'])
def test_choose_difficulty_non_integer_input(mock_input):
    result = sample_quiz.choose_difficulty()
    assert result == "Medium"

def test_validate_ans_incorrect():
    quiz = Quizzes(quiz1_ans_easy, [], [], [], [], [])
    assert quiz.validate_ans("42", quiz1_ans_easy, 0) is False

def test_validate_ans_out_of_index():
    quiz = Quizzes(quiz1_ans_easy, [], [], [], [], [])
    assert quiz.validate_ans("50", quiz1_ans_easy, 1) is False

# Test with non-numeric answers
def test_validate_ans_non_numeric():
    quiz = Quizzes(quiz1_ans_easy, [], [], [], [], [])
    assert quiz.validate_ans("apple", quiz1_ans_easy, 0) is False

if __name__ == "__main__":
    pytest.main()