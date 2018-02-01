
import sys
from parseInput import parseInput
from myMath import rac

if len(sys.argv) < 2:
    print("you need to pass at list 1 argument.")
    quit()
coeff = parseInput(sys.argv)

if (coeff == None):
    print("error")
    quit()

size = len(coeff)
if size > 3:
    print("equation de degre : " + str(size - 1) + "\nJe suis trop bete pour le resoudre")
    quit()

a = coeff[2] if size == 3 else 0
b = coeff[1] if size >= 2 else 0
c = coeff[0]

print( str(a) + "*X^2 + "+ str(b)+"*X + "+str(c) + " = 0")

print("polynome de degre " + str(size - 1))

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

print("Disc = " + str(dis))
print("rac = " + str(rac(dis)))

if (dis == 0):
    print ("Disc = 0 : racine double")
    print("X = - B / 2A")
    print("\nX = " + str(-b/(2*a)))
elif (dis > 0):
    print ("Disc > 0 : deux racines reelles ")
    print("X1 = -B -sqrt(Disc) / 2A  ;  X2 = -B +sqrt(Disc) / 2A")
    print("\nX1 = " + str((-b-rac(dis))/(2*a)))
    print("X2 = " + str((-b+rac(dis))/(2*a)))
elif (dis < 0):
    print ("Disc < 0 : deux racines complexes ")
    print("X1 = -B -i * sqrt(Disc) / 2A  ;  X2 = -B + i * sqrt(Disc) / 2A")
    if (a > 0):
        print("\nX1 = " + str(-b/(2*a)) + " - i * " + str(rac(-dis)/(2*a)))
        print("X2 = " + str(-b/(2*a)) + " + i * " + str(rac(-dis)/(2*a)))
    else:
        print("\nX1 = " + str(-b/(2*a)) + " - i * " + str(rac(-dis)/(-2*a)))
        print("X2 = " + str(-b/(2*a)) + " + i * " + str(rac(-dis)/(-2*a)))

print("\nvoila")

