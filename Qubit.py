# -*- coding: utf-8 -*-

class Qubit(object):
    
    def _init_(self):
        self._state = None
        self._process = None
        
    @property
    def state(self):
        return self._state
    
    @property
    def process(self):
        return self._process
    
    
    @state.setter
    def state(self,state):
        self._state = state
    
    @process.setter
    def process(self, process):
        self._process = process
    
    
        