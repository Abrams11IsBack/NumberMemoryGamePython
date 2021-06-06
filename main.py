import random
import time

print("Remember the following numbers in order")

int1 = random.randint(1, 1000)
int2 = random.randint(1, 1000)
int3 = random.randint(1, 1000)
int4 = random.randint(1, 1000)
int5 = random.randint(1, 1000)

print("Number 1: " + str(int1))
print("Number 2: " + str(int2))
print("Number 3: " + str(int3))
print("Number 4: " + str(int4))
print("Number 5: " + str(int5))
print("You have 15 seconds to remember the numbers...")
time.sleep(15)
for x in range(50):
  print("====================================================================")
print("Type in the numbers you remembered in order")
input1 = input("Number 1: ")
input2 = input("Number 2: ")
input3 = input("Number 3: ")
input4 = input("Number 4: ")
input5 = input("Number 5: ")
print("Checking...")
if int(input1) == int1:
    print("Number 1 is correct!")
else:
    print("Number 1 is incorrect...")
if int(input2) == int2:
    print("Number 2 is correct!")
else:
    print("Number 2 is incorrect...")
if int(input3) == int3:
    print("Number 3 is correct!")
else:
    print("Number 3 is incorrect...")
if int(input4) == int4:
    print("Number 4 is correct!")
else:
    print("Number 4 is incorrect...")
if int(input5) == int5:
    print("Number 5 is correct!")
else:
    print("Number 5 is incorrect...")
