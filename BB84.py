# -*- coding: utf-8 -*-

from Actors import Actors
    
class BB84(object):
    
    def BB84(self,n):
        actors = Actors()
        Alice = ""
        Bob = ""
        for i in range(n):
            qubitSend = actors.Alice()
            qubitReceive = actors.Bob(qubitSend)
            Alice += str(qubitSend.state)
            Bob += str(qubitReceive)   
        return Alice, Bob

    def BB84_with_Eve(self,n):
        actors = Actors()
        Alice = ""
        Bob = ""
        for i in range(n):
            qubitSend = actors.Alice()
            qubitReceiveByEve = actors.Eve(qubitSend)
            eveChoice = actors.EveChoice(qubitReceiveByEve) 
            qubitReceiveByBob = actors.Bob(eveChoice)
            Alice += str(qubitSend.state)
            Bob += str(qubitReceiveByBob)    
        return Alice, Bob


    def BB84_with_2_Eves(self,n):
        actors = Actors()
        Alice = ""
        Bob = ""
        for i in range(n):
            qubitSend = actors.Alice()
            qubitReceiveByEve = actors.Eve(qubitSend)
            eveChoice = actors.EveChoice(qubitReceiveByEve)
            qubitReceiveByEve2 = actors.Eve(eveChoice)
            eveChoice2 = actors.EveChoice(qubitReceiveByEve2) 
            qubitReceiveByBob = actors.Bob(eveChoice2)
            Alice += str(qubitSend.state)
            Bob += str(qubitReceiveByBob)         
        return Alice, Bob







