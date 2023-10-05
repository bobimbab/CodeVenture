class Game:
    """
    Game is a class for managing and playing a learning module-based game.

    Attributes:
        difficulty (list): A list of available game difficulties.
        title (str): The title or name of the learning modules.
        learning_modules (list): A list of learning modules or lessons included in the game.
        game_difficulty (str): Stores the player's chosen game difficulty.
        select_learning_module (str): Stores the selected learning module.

    Methods:
        __init__(self, title: str, learning_modules: list):
            Initialize a new Game object.

        play_game(self):
            Play the game and provide a preview of game content.

        pause_game(self):
            Pause the game.

        choose_game_difficulty(self):
            Prompt the user to select their game difficulty.

        choose_lm(self):
            Prompt the user to select the desired learning module.

    """
    difficulty = ["Easy","Medium","Hard"]

    def __init__(self, title:str, learning_modules: list):
        """
        Initialize a new Game object.

        Args:
            title (str): The title or name of the learning modules.
            learning_modules (list): A list of learning modules or lessons included in the game.
        """
        self.title = title
        self.game_difficulty = None
        self.learning_modules = learning_modules
        self.difficulty = None
        self.select_learning_module = None

    def play_game(self):
        """
        * call Challenge class to display challenges
        * call Character_details class to display characters
        * pauses the game if needed
        * tracks and record progress and achievements if needed

        Play the game and provide a preview of game content.

        Returns:
            None
        """
        print("Play game...")
        print("Coming soon!\n"
              "-------------------------------\n"
              "Preview of game content:\n \n"
              "Class is a blueprint or a template forC creating objects (instances). \n"
              "It defines a set of attributes (variables) and methods (functions) that the objects created from the "
              "class will have. \n"
              "Classes are fundamental to object-oriented programming (OOP) and are used to model real-world entities "
              "and their behaviors.\n"
              "\n"
              "Example: \n"
              "class Dog: \n"
              "     # Constructor method to initialize the object\n"
              "     def __init__(self, name, age):\n"
              "         self.name = name    # Attribute\n"
              "         self.age = age      # Attribute\n"
              "     # Method to make the dog bark\n"
              "     def bark(self):\n"
              "         print(self.name + 'says Woof!')\n"
              "End of preview\n")


    def pause_game(self):
        """
        Pause the game.

        Returns:
            None
        """
        print("Pause game...")

    def choose_game_difficulty(self):
        """
        Prompt the user to select their game difficulty.

        Returns:
            str: The chosen game difficulty.
        """
        while True:
            print("-------------------------------")
            print("Please choose your difficulty: ")
            print("\t1. Easy")
            print("\t2. Medium")
            print("\t3. Hard")

            try:
                user_input = int(input("Please select difficulty by their number. For example, '1' for Easy mode: "))
                if user_input > 3 or user_input < 1:
                    print("Please choose either Easy, Medium or Hard")
                else:
                    break
            except:
                if user_input == "q":
                    break
                print("Please enter a valid number")
        self.game_difficulty = Game.difficulty[user_input-1]
        print("You have chosen", self.game_difficulty)
        return self.game_difficulty

    def choose_lm(self):
        """
        Prompt the user to select the desired learning module.

        Returns:
            str: The selected learning module.
        """
        for idx, module in enumerate(self.learning_modules, start=1):
            print(f"{idx}. {module}")
        while True:
            try:
                user_input = int(input("Please select your learning module: "))
                self.select_learning_module = self.learning_modules[user_input-1]
                break
            except:
                print("Invalid Input!")
        return self.select_learning_module


if __name__ == "__main__":
    pass