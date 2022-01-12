import random


class NumberGuessingGame:

    def __init__(self):
        ## define the range
        self.LOWER = 1
        self.HIGHER = 9

    ## method to generate the random number
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    ## game start method
    def start(self):
        ## generating the random number
        random_number = self.get_random_number()

        print(
            f"Guess the number from {self.LOWER} to {self.HIGHER}")

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    "nice, you got the number.")
                break
            elif user_number < random_number:
                print("-> Too close yet too far")
            else:
                print("-> You are currently at the far away horizons")
            chances += 1
            
          
            

numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()