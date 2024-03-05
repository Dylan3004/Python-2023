stdin = input(str())
odd = []
even = []
lower = []
upper = []
for element in stdin:
    if element.isdigit():
        if int(element) % 2 == 1:
            odd += element
        else:
            even += element
    else:
        if element.isupper():
            upper += element
        else:
            lower += element
upper.sort()
lower.sort()
odd.sort()
even.sort()
lower = ''.join(lower)
upper = ''.join(upper)
odd = ''.join(odd)
even = ''.join(even)
print(lower + upper + odd + even)
