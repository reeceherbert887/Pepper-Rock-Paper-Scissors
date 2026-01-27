import random

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        resetMatch
        

        def resetMatch(self):
            self.gameStart = False
            self.userScore = 0
            self.pepperScore = 0
            self.roundsPlayed = 0

    # Input: onStart (bang)
    def onInput_onStart(self):
        # Once head sensor is activated, game starts
        self.resetMatch()
        self.sayText("Would you like to play Rock, Paper, Scissors? Best of three. Please say yes or no.")
        self.onStopped()

    # Input: onStop (bang)
    def onInput_onStop(self):
        self.onStopped()

    def onInput_onUserMove(self, value):
        user = value[0] if isinstance(value, (list, tuple)) else value
        user = str(user).lower().strip()

        # Invitation stage
        if not self.gameStart:
            if user == "yes":
                self.gameStart = True
                self.sayText("Okay, let's begin. Please say rock, paper, or scissors.")
                return

            elif user in ["no", "stop", "quit"]:
                self.sayText("Okay, thank you. Goodbye.")
                self.end()
                return

            else:
                self.sayText("Please say yes or no.")
                return

        # Does not go over 2 rounds
        if self.roundsPlayed >= 3:
            # If something breaks
            self.sayText("This match is finished.")
            return()


        #Game mode
        if user not in ["rock", "paper", "scissors"]:
            self.sayText("Sorry, I didn't catch that. Please say rock, paper, or scissors.")
            return

        pepper = random.choice(["rock", "paper", "scissors"])
        self.roundsPlayed += 1

         # Decide outcome and update scores
        if user == pepper:
            outcome = "It's a draw."
            self.doDraw()
        elif (user == "rock" and pepper == "scissors") or \
             (user == "paper" and pepper == "rock") or \
             (user == "scissors" and pepper == "paper"):
            outcome = "You win this round."
            self.userScore += 1
            self.doSad()   # Pepper is sad because user won
        else:
            outcome = "I win this round."
            self.pepperScore += 1
            self.doHappy() # Pepper is happy because it won

        # Pepper shows its chosen move (gesture timeline)
        if pepper == "rock":
            self.doRock()
        elif pepper == "paper":
            self.doPaper()
        else:
            self.doScissors()

        # Send to tablet UI
        scoreLine = "You: {} - Me: {}".format(self.userScore, self.pepperScore)

        self.scoreText(scoreLine)

        self.sayText("You chose {}. I chose {}. {} {}".format(user, pepper, outcome, ))

        # --- End conditions ---
        # 1) First to 2 wins (best of three)
        if self.userScore >= 2 or self.pepperScore >= 2:
            self._finishMatch()
            return

        # 2) Hard cap after 3 rounds (prevents “4th round” after draws)
        if self.roundsPlayed >= 3:
            # Decide overall winner (could be draw)
            if self.userScore > self.pepperScore:
                self.sayText("You win overall.")
            elif self.pepperScore > self.userScore:
                self.sayText("I win overall.")
            else:
                self.sayText("It's a draw overall.")
            self._finishMatch()
            return

        # Continue prompt (short)
        self.sayText("Next one. Rock, paper, or scissors?")

    def _finishMatch(self):
        self.scoreText("Match finished. Say yes to play again, or no to quit.")
        self.resetMatch()
        self.sayText("Would you like to play again? Say yes or no.")