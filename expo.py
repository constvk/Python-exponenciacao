import os

def sum(x, y):
    return x ** y

print("exponenciação de dois números")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

print ("")
print ("O resultado da exponenciação é %d" %sum(x, y))

os.system("pause")
