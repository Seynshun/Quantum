# -*- coding: utf-8 -*-
from random import randint, choice
from Qubit import Qubit
Process = [1,2]

class Actors(object):
    
    def Bob(self,qubit):
        try:
            if (qubit.process == choice(Process)):
                return qubit.state
            else:
                return randint(0, 1)
        except:
            return randint(0, 1)

    def Eve(self,qubit):
        return self.Bob(qubit)
    
    def EveChoice(self,qubit):
        eveChoice = Qubit()
        try:
            eveChoice.state = qubit.state
        except:
            eveChoice.state = qubit
        eveChoice.process = choice(Process)
        return eveChoice
            
    def Alice(self):
        qubit = Qubit()
        qubit.state = randint(0,1)
        qubit.process = choice(Process)
        return qubit
