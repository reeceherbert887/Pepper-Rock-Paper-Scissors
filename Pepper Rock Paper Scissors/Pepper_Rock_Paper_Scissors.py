from ipaddress import v4_int_to_packed
import random
from unittest import result

class MyClass(GeneratedClass):
    def __init__ (self):
        GeneratedClass.__init__(self)

    def OnLoad(self):
        pass

    def OnUnload(self):
        pass
    
    def OnInput_Start(self):
        # Once head sensor is activates game starts
        self.SayText("Lets play a game of Rock, Paper, Scissors!")
        self.OnStopperd()

    def OnInput_Stopped(self):
        self.OnLoad()
        self.OnUnload()

    def OnInput_User(self, value):
        # Speech, recognition, yes, no yes: starts the game | no: goes into standby

        User = value

        if isinstance (value, list) or isinstance(value, tuple):
            User = value[0]
        
        User = str(User).lower().strip()

        if User in ["no", "stop"]:
            self.SayText("Ok, Thank you")
            self.End()
            return

        if User not in ["rock", "paper", "scissors"]:
            self.SayText("Sorry, I didn't quire catch that. Please say rock, paper, or scissors.")
            self.PlayAgain()

        Pepper = random.choice(["rock", "paper", "scissors"])

        if User == Pepper:
            result = "It's a draw!"

        elif (User == "rock" and Pepper == "scissors") or \
             (User == "paper" and Pepper == "rock") or \
             (User == "scissors" and Pepper == "scissors"):
             result = "You win!"
        else:
            result = "I Win!"
          