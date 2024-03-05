def fun():
    number = int(input('Enter the number '))
    temp = str(binary(number))
    length = len(temp)
    the_greatest = 0
    curr = 0

    for i in range(len(temp)):
        if temp[i] == "0":
            curr += 1
        else:
            if curr > the_greatest:
                the_greatest = curr
            curr = 0

    if curr > the_greatest:
        the_greatest = curr

    print("The greatest number of zeros in a row:",str(the_greatest))




def binary(num):
    # deciman number to binary
    binary_string = ""
    while num != 0:
        prev_num = num
        num = num // 2
        if prev_num != num*2:
                binary_string+="1"
        else:
            binary_string+="0"
    binary_string = binary_string[::-1]
    print(binary_string)
    return binary_string


fun()
