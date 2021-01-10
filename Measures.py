# -*- coding: utf-8 -*-
from BB84 import BB84
import matplotlib.pyplot as plt

    
def BB84_measures(n):
    bb84 = BB84()
    (Alice,Bob) = bb84.BB84(n)
    success = 0
    for i in range(n):
        if Alice[i] == Bob[i] :
            success += 1
    return success/n *100


def BB84_with_Eve_measures(n):
    bb84 = BB84()
    Alice,Bob = bb84.BB84_with_Eve(n)
    success = 0
    for i in range(n):
        if Alice[i] == Bob[i] :
            success += 1
    return success/n *100

def BB84_with_2_Eve_measures(n):
    bb84 = BB84()
    Alice,Bob = bb84.BB84_with_2_Eves(n)
    success = 0
    for i in range(n):
        if Alice[i] == Bob[i] :
            success += 1
    return success/n *100

AliceBob = [BB84_measures(i) for i in range(100,6000, 100)]
AliceBobEve = [BB84_with_Eve_measures(i) for i in range(100,6000,100)] 
AliceBob2Eve = [BB84_with_2_Eve_measures(i) for i in range(100,6000,100)]
X = range(len(AliceBob))
plt.plot(X, AliceBob, label="With Eve")
plt.plot(X, AliceBobEve, label="Without Eve")
plt.plot(X, AliceBob2Eve, label="With 2 Eve")
plt.ylabel("Accuracy")
plt.xlabel("Measures length")
plt.legend()
plt.show()

