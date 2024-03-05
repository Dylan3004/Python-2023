

len = int(input("Enter the length of loading screan: "))
str1 = ""
str2 = ""
iter = 0
for j in range(len+1):
    print("|", end="")
    for i in range(iter):
        str1 += '='
    print(str1, end="")
    for i in range(len - iter):
        str2 += "-"
    print(str2, end="")
    print("| ", end="")
    print(str(int(iter/len*100))+"%")

    str1 = ""
    str2 = ""
    iter += 1


