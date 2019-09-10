print("Välkommen till mitt räknet program")

operator = input("Välj räknesätt +, -, *, / : ")

try:
    num1 = int(input('Mata in ett helt tal: '))
except:
    print("Du måste skriva in ett heltal: ")
    num1 = 0

try:
    num2 = int(input('Mata in ett till heltal: '))
except:
    print("Du måste skriva in ett heltal: ")
    num2 = 0

if operator == "+":
    summa = num1 + num2

elif operator == "-":
    summa = num1 - num2

elif operator == "*":
    summa = num1 * num2

elif operator == "/":
    try: 
        summa = num1 / num2
    except(ZeroDivisionError):
        print("Det går inte att dela me 0")
        summa = str(" fel lol")

else:
    print("FEL")

print("summa är:" + str(summa))