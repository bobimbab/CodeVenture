import pytest
from datetime import date
from interface import Interface
from user import User, Admin, YoungLearner

# Sample data for testing
# sample_users_dict = {
#     "admin": Admin("Admin", "User", date(1990, 1, 1), "admin@example.com", "1990-01-01", "admin@mail.com", "012345678"),
#     "learner": YoungLearner("Learner", "User", date(2003, 3, 15), "learner@example.com", "2003-03-15", "dk@mail.com", "011111111", "7")
# }

def test_is_leap_year():
    assert Interface.is_leap_year(2000) == True
    assert Interface.is_leap_year(2024) == True
    assert Interface.is_leap_year(1900) == False
    assert Interface.is_leap_year(2022) == False

def test_date_value_check():
    assert Interface.date_value_check(2000, 2, 29) == True
    assert Interface.date_value_check(2024, 2, 29) == False
    assert Interface.date_value_check(1900, 2, 29) == False
    assert Interface.date_value_check(2022, 2, 29) == False

def test_ph_num_check():
    assert Interface.ph_num_check("1234567890") == "1234567890"
    assert Interface.ph_num_check("9876543210") == "9876543210"
    assert Interface.ph_num_check("12345") is None
    assert Interface.ph_num_check("12345678901") is None

def test_email_check():
    assert Interface.email_check("test@example.com") == True
    assert Interface.email_check("user@domain") == False
    assert Interface.email_check("invalid_email") == False
    assert Interface.email_check("example.com") == False

def test_grade_check():
    assert Interface.grade_check("8") == 8
    assert Interface.grade_check("12") == 12
    assert Interface.grade_check("0") is None
    assert Interface.grade_check("13") is None

if __name__ == '__main__':
    pytest.main()
