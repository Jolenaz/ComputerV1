
import sys
from parseInput import parseInput

if len(sys.argv) < 2:
    print("you need to pass at list 1 argument.")
    quit()
coeff = parseInput(sys.argv)

if (coeff != 10):
    print("error")
    quit()

print("ok bro")

