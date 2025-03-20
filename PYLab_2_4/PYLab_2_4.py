import random as rand

print("Input the value of attempts")
AttCount = int(input())
x = rand.randint(0, 100)
print("Guess the value of X:")
TotalAttCount = 0
CurrentNum = -1;

while (TotalAttCount != AttCount) and (CurrentNum != x):
    CurrentNum = int(input("Input number:"))
    TotalAttCount += 1
    if (CurrentNum > x):
        print("The value of x is smaller, try again:")
    elif (CurrentNum < x):
        print("The value of x is bigger, try again: ")

if (CurrentNum != x):
    print("X was", x, "count of attempts is", TotalAttCount)
else:
    print("You won! X was", x, "total count of attempts is", TotalAttCount)
