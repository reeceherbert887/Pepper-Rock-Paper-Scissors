from pickle import FALSE
import random

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.gameStart = False
        self.userScore = 0
        self.pepperScore = 0
        self.roundsPlayed = 0

    #def onLoad(self):
        #pass

   # def onUnload(self):
        #pass

    # Input: onStart (bang)
    def onInput_onStart(self):
        # Once head sensor is activated, game starts
        self.gameStart = False
        self.userScore = 0
        self.pepperScore = 0
        self.roundsPlayed = 0
        self.sayText("Let's play Rock, Paper, Scissors! Say rock, paper, or scissors.")
        #self.playAgain()  # start listening
        self.onStopped()

    # Input: onStop (bang)
    def onInput_onStop(self):
        self.onUnload()
        self.onStopped()

    def onInput_onUserMove(self, value):
        user = value[0] if isinstance(value, (list, tuple)) else value
        user = str(user).lower().strip()

        # Invitation stage
        if not self.game_started:
            if user == "yes":
                self.game_started = True
                self.sayText("Okay, let's begin. Please say rock, paper, or scissors.")
                return
            elif user in ["no", "stop", "quit"]:
                self.sayText("Okay, thank you. Goodbye.")
                self.end()
                return
            else:
                self.sayText("Please say yes or no.")
                return


        #Game mode
        if user not in ["rock", "paper", "scissors"]:
            self.sayText("Sorry, I didn't catch that. Please say rock, paper, or scissors.")
            self.playAgain()
            return

        pepper = random.choice(["rock", "paper", "scissors"])
        self.roundsPlayed += 1

        if user == pepper:
            outcome = "It's a draw!"
        elif (user == "rock" and pepper == "scissors") or \
             (user == "paper" and pepper == "rock") or \
             (user == "scissors" and pepper == "paper"):
            outcome = "You win!"
            userScore += 1
        else:
            outcome = "I win!"
            pepperScore += 1

        self.sayText("You chose " + user + "I chose " + pepper + " " + outcome + "The score is now " + str(self.userScore) + "Me " + str(self/pepperScore) +  "")

        # Trigger Pepper's chosen gesture
        if pepper == "rock":
            self.doRock()
        elif pepper == "paper":
            self.doPaper()
        else:
            self.doScissors()

        self.playAgain()

        if self.userScore == 2:
            self.sayText ("Congraulations! You've beaten me for now")
            self.game_started = False
            self.userScore = 0
            self.pepperScore = 0
            self.sayText("Would you like to play again? Please say yes or no.")
            return

        if self.pepperScore == 2:
            self.sayText("I have won! better luck next time")
            self.game_started = False
            self.userScore = 0
            self.pepperScore = 0
            self.sayText("Would you like to play again? Please say yes or no.")
            return