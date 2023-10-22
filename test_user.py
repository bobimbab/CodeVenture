from datetime import date
import pytest
from user import User, YoungLearner, Admin

# Define test data
user_data = {
    'user1': User('John', 'Doe', 'user1', 'password123', date(1990, 1, 1), 'john@example.com', '1234567890'),
    'user2': User('Alice', 'Smith', 'user2', 'secret', date(1985, 5, 5)),
}

young_learner_data = {
    'learner1': YoungLearner('Learner', 'One', 'learner1', 'childpass', date(2010, 10, 10), 'learner@example.com', '9876543210', 3),
}

admin_data = {
    'admin1': Admin('Admin', 'User', 'admin1', 'adminpass', date(1975, 8, 8), 'admin@example.com', '1112223333'),
}


def test_user_registration_successful():
    users_dict = {}
    result = User.register(users_dict, 'Alice',
                           'Smith',
                           'alice',
                           'secret',
                           date(1985, 5, 5),
                           'alism@mail.com',
                           '011112345')
    assert result is True
    assert 'alice' in users_dict

def test_user_registration_failed():
    users_dict = {'user2': user_data['user2']}
    result = User.register(users_dict, 'Alice',
                           'Smith',
                           'user2',
                           'secret',
                           date(1985, 5, 5),
                           'alism@mail.com',
                           '011112345')
    assert result is False

def test_user_authentication_successful():
    users_dict = {'user1': user_data['user1']}
    result = User.authenticate(users_dict,
                               'user1',
                               'password123')
    assert result is True

def test_user_authentication_failed():
    users_dict = {'user1': user_data['user1']}
    result = User.authenticate(users_dict,
                               'user1',
                               'wrong_password')
    assert result is False

# YoungLearner class test
def test_young_learner_creation():
    learner = YoungLearner('Learner',
                           'One',
                           'learner1',
                           'childpass',
                           date(2010, 10, 10),
                           'learner@example.com',
                           '9876543210', 3)
    assert learner.first_name == 'Learner'
    assert learner.grade == 3  # Additional attribute for YoungLearner

# Admin class tests
def test_admin_creation():
    admin = Admin('Admin',
                  'User',
                  'admin1',
                  'adminpass',
                  date(1975, 8, 8),
                  'admin@example.com',
                  '1112223333')
    assert admin.first_name == 'Admin'

if __name__ == '__main__':
    pytest.main()
