import unittest
from interface import Interface
# from quizzes import Quizzes
from unittest.mock import patch
from io import StringIO

class TestUserRegistration(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', 'Alice',
                                          'Smith', '2000', '5',
                                          '10', 'alice', 'password',
                                          'alice@example.com',
                                          '1234567890', '1', 'q'])
    def test_user_registration(self, mock_input):
        interface = Interface()

        # Perform user registration
        interface.main_menu()

        # Verify that the registered user exists in the users_dict
        self.assertTrue('alice' in interface.users_dict)

class TestUserLogin(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'johndoe', 'pw', '4', 'q'])
    def test_user_login(self, mock_input):
        interface = Interface()

        # Perform user login
        interface.main_menu()

        # Verify that the logged-in user's username is set correctly
        self.assertEqual(interface.current_user, 'johndoe')

class TestUserProfileView(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'johndoe', 'pw', '1', '4', 'q'])
    def test_user_profile_view(self, mock_input):
        interface = Interface()

        # Redirect stdout to capture printed messages
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Perform user login
            interface.main_menu()
            # Navigate to the profile view option
            output = mock_stdout.getvalue()

        # Check if the user's profile details are present in the captured output
        self.assertIn("User: John Doe", output)
        self.assertIn("Username: johndoe", output)
        self.assertIn("Date of Birth: 2001-07-28", output)
        self.assertIn("Email: john@gmail.com", output)
        self.assertIn("Phone Number: 0123456789", output)
        self.assertIn("Grade: 10", output)


# class TestUserPlayQuiz(unittest.TestCase):
#     @patch('builtins.input', side_effect=['1', 'johndoe', 'pw', '3', '1', '50', '3.0', '1', '4', 'q'])
#     def test_user_play_quiz(self, mock_input):
#         interface = Interface()
#         # Redirect stdout to capture printed messages
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             # Perform user login
#             interface.main_menu()
#             # Navigate to the quizzes menu
#             interface.quiz_menu()
#
#             output = mock_stdout.getvalue()
#
#         # Check if the quiz results or success message is present in the captured output
#         self.assertIn("Answer is correct!", output)
#         self.assertIn("Congratulations on finishing the quiz!", output)

class TestUserPlayGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'johndoe', 'pw', '2', '1', '4', 'q'])
    def test_user_play_game(self, mock_input):
        interface = Interface()
        # Redirect stdout to capture printed messages
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Perform user login
            interface.main_menu()
            # Navigate to the game menu
            interface.game_menu()

            # Start the game
            output = mock_stdout.getvalue()
            self.assertIn("Preview of game content:", output)
            self.assertIn("End of preview:", output)

if __name__ == '__main__':
    unittest.main()
