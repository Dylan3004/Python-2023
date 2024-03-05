import numpy as np
import matplotlib.pyplot as plt

# Określenie zakresu wartości x
sentence = str(input("Write a polynomial: "))
x_min = int(input("Write a minimum value of x: "))
x_max = int(input("Write a maximum value of x: "))

# Wygenerowanie tablicy wartości x
x_val = np.linspace(x_min, x_max, 200)

# Wielomian jako ciąg znaków


# Obliczenie wartości dla tablicy x_val
y_val = []
for x in x_val:
    try:
        y_val.append(eval(sentence))
    except Exception as e:
        print("Wrong polynomial [", e, "]")
        exit(1)


# Narysowanie wykresu
plt.figure(figsize=(9, 7))
plt.plot(x_val, y_val, label=sentence)
plt.xlabel('Values of x')
plt.ylabel('Values of y')
plt.title('Figure of polynomial : ' + sentence)
plt.legend()
plt.grid(True)
plt.show()