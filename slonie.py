import numpy as np
from numpy import int64

n = int(input()) # liczba słoni

weight = np.empty(n, dtype=int64)
pos = np.empty(n, dtype=int64)  # pozycje słoni
perm = np.empty(n, dtype=int64) #permutacja pozycji słoni

for i in range(n):
    weight[i] = int(input())
minWeight = min(weight) # minimalna waga 

for i in range(n):
    pos[i] = int(input()) - 1

for i in range(n):
    number = int(input())
    perm[ number - 1 ] = pos[i]

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
