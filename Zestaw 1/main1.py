import sys  # importujemy modul


def generator(n):  # generator
    list = []
    for num in range(2, n+1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            list.append(num)
    return list

def answear(number):
    primes = (generator(number))
    primes_list = []
    #print(primes)
    for i in range(len(primes)):
        primes_list.append(0)
        # print(primes)
    # print(primes_list)
    temp_number = number

    iter = 1
    jump = 0
    while temp_number != 1:
        if temp_number % primes[jump] == 0:
            #print("Number before" + str(temp_number))
            temp_number = temp_number / primes[jump]
            #print("Nubmer after" + str(temp_number))
            primes_list[jump] += 1
            iter += 1
        else:
            iter = 1
            jump += 1
            #print(temp_number)
        if temp_number == 1 or jump == len(primes):
            break

    #print(primes_list)
    print("Number: " + str(number) + " as primal multiplication is:", end="")
    for i in range(len(primes)):
        if primes_list[i] != 0:
            print(str(primes[i]) + "^" + str(primes_list[i]), end="")
            for j in range(i + 1, len(primes)):
                if primes_list[j] != 0:
                    print("*", end="")
                    break

argv = sys.argv[1:]  # argv to lista, a 1: robi selekcje bez pierwszego argumentu – nazwy programu
print(argv)
arguments = []
for i in range(len(argv)):  # za pomoca generatora
    if (int(argv[i])) > 2:
        answear(int(argv[i]))
        print()
    else:
        print("You write a number lower than 2")
        break
      # wpisujemy, rzutowanie z typu str na int przyda sie potem

