
import sys
import math
from parseInput import parseInput

if len(sys.argv) < 2:
    print("you need to pass at list 1 argument.")
    quit()
coeff = parseInput(sys.argv)

if (coeff == None):
    print("error")
    quit()

print( str(coeff[2]) + "*X^2 + "+ str(coeff[1])+"*X + "+str(coeff[0]) + " = 0")

a = coeff[2]
b = coeff[1]
c = coeff[0]

if (a == 0):
    if (b == 0):
        if (c == 0):
            print("Ensemble des reels est solution.")
            quit()
        else:
            print("Ensemble vide est solution")
            quit()
    else:
        print("Equation du premier degre")
        print("X = " + str(-c/b))
        quit()

print("Discriminent : B^2 - 4AC")

dis = b * b - 4 * a * c 

print("Disc =" + str(dis))

if (dis == 0):
    print ("Disc = 0 : racine double")
    print("X = - B / 2A")
    print("X = " + str(-b/(2*a)))
elif (dis > 0):
    print ("Disc > 0 : deux racines reelles ")
    print("X1 = -B -sqrt(Disc) / 2A  ;  X2 = -B +sqrt(Disc) / 2A")
    print("X1 = " + str((-b-math.sqrt(dis))/(2*a)))
    print("X2 = " + str((-b+math.sqrt(dis))/(2*a)))
elif (dis < 0):
    print ("Disc < 0 : deux racines complexes ")
    print("X1 = -B -i * sqrt(Disc) / 2A  ;  X2 = -B + i * sqrt(Disc) / 2A")
    print("X1 = " + str(-b/(2*a)) + " - i * " + str(math.sqrt(-dis)/(2*a)))
    print("X2 = " + str(-b/(2*a)) + " + i * " + str(math.sqrt(-dis)/(2*a)))
print("voila")

