import os

os.system("cls")
print("Input an integer number:")
iNum = int(input())
iVal = abs(iNum)
nDigits = 0
while (iVal > 0):
    iVal //= 10
    nDigits += 1

print(f"The number {iNum} has {nDigits} digit(s)")