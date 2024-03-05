
x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
z = int(input("Enter the z value: "))
n = int(input("Enter the n value: "))
table = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if i+j+k<n:
                temp_table=[i,j,k]
                table.append(temp_table)


print(table)
