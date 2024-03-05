import math

length = int(input("Enter a length: "))
print("|",end="")
for i in range(length):
    print("....|",end="")
print()
void=4
num =0
for i in range(length+1):
    print(str(num) + void*" ",end="")
    num1=num
    num+=1
    if len(str(num+1)) > len(str(num)):
        void-=1


