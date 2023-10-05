class Quizzes:
    """
    Quizzes is a class for managing and conducting quizzes of different difficulties.

    Attributes:
        difficulty (list): A list of available quiz difficulties.
        ans_easy (list): A list of correct answers for easy questions.
        ans_medium (list): A list of correct answers for medium questions.
        ans_hard (list): A list of correct answers for hard questions.
        easy_questions (list): A list of easy quiz questions.
        medium_questions (list): A list of medium quiz questions.
        hard_questions (list): A list of hard quiz questions.
        player_difficulty (str): Stores the player's chosen difficulty level.

    Methods:
        __init__(self, ans_easy, ans_medium, ans_hard, easy_questions, medium_questions, hard_questions):
            Initialize a new quiz.

        display_menu(self):
            Display the main menu for the quiz.

        choose_difficulty(self) -> None:
            Prompt the user to select their difficulty for the quiz.

        display_questions(self, questions, correct_answers):
            Display quiz questions and validate user answers.

        play_quiz(self) -> None:
            Start the quiz based on the selected difficulty.

        validate_ans(self, user_ans: str, answer: list, index) -> bool:
            Validate user answers against correct answers for a quiz question.

        start_quiz():
            Start a sample quiz for the system.

    """
    difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, ans_easy, ans_medium, ans_hard, easy_questions, medium_questions, hard_questions):
        """Initialises a new quiz

        Args:
            ans_easy (list): A list of correct answers for easy questions.
            ans_medium (list): A list of correct answers for medium questions.
            ans_hard (list): A list of correct answers for hard questions.
            easy_questions (list): A list of easy quiz questions.
            medium_questions (list): A list of medium quiz questions.
            hard_questions (list): A list of hard quiz questions.
            player_difficulty (str): Stores the player's chosen difficulty level.

        """
        self.ans_easy = ans_easy
        self.ans_medium = ans_medium
        self.ans_hard = ans_hard
        self.easy_questions = easy_questions
        self.medium_questions = medium_questions
        self.hard_questions = hard_questions
        self.player_difficulty = None

    def display_menu(self):
        """
        Display the main menu for the quiz.
        """
        print("-----Welcome to CODEVENTURE QUIZZES!-----")

    def choose_difficulty(self) -> None:
        """
        Prompt the user to choose a quiz difficulty.

        Returns:
            None
        """
        while True:
            print("-------------------------------")
            print("Please choose your difficulty")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            user_input = input("Please select difficulty by their number. For example, '1' for Easy mode: ")
            try:
                user_input = int(user_input)
                if user_input > 3 or user_input < 1:
                    print("Please choose either Easy, Medium or Hard")
                else:
                    break
            except:
                if user_input == "q":
                    print("You have quit the quiz!")
                    return

        self.player_difficulty = Quizzes.difficulty[user_input - 1]
        print("You have choosen", self.player_difficulty)
        return self.player_difficulty

    def display_questions(self, questions, correct_answers):
        """
        Display quiz questions and validate user answers.

        Args:
            questions (list): List of questions to display.
            correct_answers (list): List of correct answers for the questions.

        Returns:
            None
        """
        exit_game = False
        for i in range(len(questions)):
            if exit_game is True:
                break
            while True:
                print("QUESTION NUMBER", i + 1)
                print(questions[i])
                user_ans = input("Please input an answer: ")
                if self.validate_ans(user_ans, correct_answers, i):
                    print("Answer is correct!")
                    break
                elif user_ans == "q":
                    exit_game = True
                    break
                else:
                    print("Answer is wrong!")

        if exit_game:
            print("Exiting the game.")

        if not exit_game:
            print("Congratulations on finishing the quiz!")



    def play_quiz(self) -> None:
        """
        Start the quiz based on the selected difficulty.

        Returns:
            None
        """
        # display easy questions
        if self.player_difficulty == "Easy":
            self.display_questions(self.easy_questions, self.ans_easy)
        # display medium questions
        elif self.player_difficulty == "Medium":
            self.display_questions(self.medium_questions, self.ans_medium)
        # display hard questions
        elif self.player_difficulty == "Hard":
            self.display_questions(self.hard_questions, self.ans_hard)
        else:
            print("Please select your difficulty before you begin!")


    def validate_ans(self, user_ans: str, answer: list, index) -> bool:
        """
        Validate user answers against correct answers for a quiz question.

        Args:
            user_ans (str): User-provided answer.
            answer (list): List of correct answers.
            index: Index of the current question.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        # check if the questions are equal to the answer
        if user_ans == answer[index]:
            return True
        else:
            return False

    @staticmethod
    def start_quiz():
        """
        Start a sample quiz for the system.
        """
        # sample data
        quiz1_ans_easy = ["50", "3.0", "1"]
        quiz1_ans_medium = ["d", "b", "b"]
        quiz1_ans_hard = ["q", "60", "65"]
        quiz1_easy_questions = ["(2 + 3) * (13 - 3) = ?", "2 ** 3 / 2 - 4 + 3", "5 // 9 + 3 % 2"]
        quiz1_medium_questions = ["""Which operator is used for exponentiation in Python?\na) + \nb) * \nc) ^ \nd) ** \n""",
        """Which of the following data types is used to store a single character in Python?\na) int\nb) str\nc) float\nd) bool\n""",
        """What is the primary purpose of a Python function?\na) To store data\nb) To perform a specific task or operation\nc) To create a class\nd) To define a loop\n
        """]

        quiz1_hard_questions = ["To be IMPLEMENTED SOON. Please input 'q' to quit"]
        new_game1 = Quizzes(quiz1_ans_easy, quiz1_ans_medium, quiz1_ans_hard, quiz1_easy_questions,
                            quiz1_medium_questions, quiz1_hard_questions)
        new_game1.display_menu()
        new_game1.choose_difficulty()
        if new_game1.player_difficulty == None:
            return
        new_game1.play_quiz()


if __name__ == "__main__":
    # initialise a new quiz with the questions and answer banks provided by the database

    pass
