import numpy as np
from numpy import int64

path = input()

with open(path, 'r') as file:
    n = int(file.readline()) # liczba słoni

    weight = np.array(file.readline().split(), dtype=int64)
    minWeight = min(weight) # minimalna waga 

    pos = np.array(file.readline().split(), dtype=int64) # pozycje słoni
    pos = pos - 1

    perm = np.empty(n, dtype=int64) #permutacja pozycji słoni
    i = 0
    for number in file.readline().split():
        perm[ int(number) - 1 ] = pos[i]
        i += 1

boolArray = np.full( n , False ) # czy pozycja w cyklu została już zbadana
score = 0 # wynik ostateczny
for i in range( n ):
    if boolArray[i] == False:
        sumOfWeights = 0 # suma wag 
        lenghtOfC = 0 # długość cyklu 
        minOfC = float('inf') # minimalna waga w danym cyklu
        index = i
        while True:
            minOfC = min( minOfC, weight[index])
            sumOfWeights += weight[index]
            index = perm[index]
            boolArray[index] = True
            lenghtOfC += 1
            if index == i:
                break
        score += min(sumOfWeights + (lenghtOfC - 2) * minOfC, sumOfWeights + minOfC + (lenghtOfC + 1) * minWeight)

print(score)
