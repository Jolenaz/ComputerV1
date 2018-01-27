
import re


def checkPowerZero(equation):
    exp = r"[\-\+=\.][0-9]+$"
    m = re.search(exp, equation)
    if m:
        rpl = m.group(0) + "X^0"
        equation = re.sub(exp, rpl,equation)

    exp = r"^([0-9]+)([\-\+=])"
    m = re.search(exp, equation)
    if m:
        rpl = m.groups()[0] + "X^0" + m.groups()[1]
        equation = re.sub(exp, rpl,equation)

    exp = r"([\-\+=\.][0-9]+)([\-\+=])"
    m = re.search(exp, equation)
    while m:
        rpl = m.groups()[0] + "X^0" + m.groups()[1]
        equation = re.sub(exp, rpl,equation,count=1)
        m = re.search(exp, equation)

    return equation

def checkEquationCaractere(equation):
    exp = r"[^0-9^+\-X=\.]"
    m = re.search(exp, equation)
    if m:
        print("Invalide chractere found : " + m.group(0))
        return False
    exp = r".+=.+"
    if re.search(exp, equation) is None:
        print("The equation must have one \"=\" signe in its midle")
        return False
    

def parseSide(data, side, coeff):
    exp = r"([\+\-]?[0-9]+\.?[0-9]?)X\^([0-9]+)"
    m = re.search(exp,data)
    while m:
        if len(coeff) < int(m.groups()[1]) + 1:
            while(len(coeff) != int(m.groups()[1]) + 1):
                coeff.append(0)
        coeff[int(m.groups()[1])] += side * float(m.groups()[0])
        rpl = ""
        data = re.sub(exp, rpl, data, 1)
        m = re.search(exp,data)
    if (data != ""):
        print("error in parsing : ", data)
        quit()
    return (coeff)

def parseInput(rawInput):
    equation = ""
    for i in range(1,len(rawInput)):
        equation += rawInput[i]
    equation = equation.replace(" ", "")
    if (equation[0] == 'X'):
        equation = "+" + equation
    if equation[len(equation) - 1] == 'X':
        equation = equation + "^1"
    equation = equation.replace("*X", "X")
    equation = equation.replace("+X", "+1X")
    equation = equation.replace("-X", "-1X")
    equation = equation.replace("X+", "X^1+")
    equation = equation.replace("X-", "X^1-")
    equation = equation.replace("X=", "X^1=")
    equation = equation.replace("=X", "=1X")

    for i in "0123456789":
        fo = "X" + i
        equation = equation.replace("X" + i, "X^" + i)
    equation = checkPowerZero(equation)
    if checkEquationCaractere(equation) == False:
        return (None)
    sides = equation.split('=')
    if (len(sides) != 2):
        print("to many \"=\"")
        return (None)

    coeff = []
    coeff = parseSide(sides[0], 1, coeff)
    coeff = parseSide(sides[1], -1, coeff)

    return (coeff)
