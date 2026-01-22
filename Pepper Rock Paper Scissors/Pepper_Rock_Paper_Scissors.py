import random

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    # Input: onStart (bang)
    def onInput_onStart(self):
        # Once head sensor is activated, game starts
        self.sayText("Let's play Rock, Paper, Scissors! Say rock, paper, or scissors.")
        self.playAgain()  # start listening
        self.onStopped()

    # Input: onStop (bang)
    def onInput_onStop(self):
        self.onUnload()
        self.onStopped()

    # Input: onUserMove (string)  connect Speech Reco wordRecognized here
    def onInput_onUserMove(self, value):
        user = value
        # Speech Reco often sends word, confidence
        if isinstance(value, (list, tuple)) and len(value) > 0:
            user = value[0]

        user = str(user).lower().strip()

        if user in ["no", "stop", "quit"]:
            self.sayText("Okay, thank you. Bye!")
            self.end()
            return

        if user not in ["rock", "paper", "scissors"]:
            self.sayText("Sorry, I didn't catch that. Please say rock, paper, or scissors.")
            self.playAgain()
            return

        pepper = random.choice(["rock", "paper", "scissors"])

        if user == pepper:
            outcome = "It's a draw!"
        elif (user == "rock" and pepper == "scissors") or \
             (user == "paper" and pepper == "rock") or \
             (user == "scissors" and pepper == "paper"):
            outcome = "You win!"
        else:
            outcome = "I win!"

        self.sayText("You chose " + user + ". I chose " + pepper + ". " + outcome)

        # Trigger Pepper's chosen gesture
        if pepper == "rock":
            self.doRock()
        elif pepper == "paper":
            self.doPaper()
        else:
            self.doScissors()

        self.playAgain()
