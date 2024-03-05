
def number_recognizer(number):
    number_table = "1234567890"
    if number[0] in number_table:
        arabic_to_roman(number)
    else:
        roman_to_arabic(number)

def arabic_to_roman(number):
    forth_level_mark = ["M"]
    third_level_mark = ["D", "C"]
    second_level_mark = ["L", "X"]
    first_level_mark = ["V", "I"]
    level_table = [forth_level_mark,third_level_mark,second_level_mark,first_level_mark]
    if int(number)>4000:
        print("Number is to big")
        return
    else:
        out = ""
        for i in range(len(number)):

            if i==3 :
                out+=int(number[len(number)-1-i])*level_table[len(level_table) - 1 - i][0]
                break
            elif int(number[len(number)-1-i])>4 and int(number[len(number)-1-i])<9:
                out += (int(number[len(number) - 1 - i]) - 5) * level_table[len(level_table) - 1 - i][1]
                out += level_table[len(level_table) - 1 - i][0]
            elif int(number[len(number)-1-i])<4:
                out += int(number[len(number)-1-i]) * level_table[len(level_table) - 1 - i][1]
            elif int(number[len(number)-1-i])==4:
                out += level_table[len(level_table) - 1 - i][0]
                out += level_table[len(level_table) - 1 - i][1]
            elif int(number[len(number)-1-i]) == 9:
                out += level_table[len(level_table) - i - 2][1]
                out += level_table[len(level_table) - 1 - i][1]
            else:
                print("bug")
        out = out[::-1]
        print(out)


def roman_to_arabic(number):
    numbers_table = [[1000,"M"],[500,"D"],[100,"C"],[50,"L"],[10,"X"],[5,"V"],[1,"I"]]
    sum =0
    reminder =0
    for i in range(len(number)):
        if i == 1:
          for j in range(len(numbers_table)):
              if numbers_table[j][1]==number[i]:
                  sum+=numbers_table[j][0]
                  reminder = numbers_table[j][0]
        else:
            for j in range(len(numbers_table)):
                if numbers_table[j][1] == number[i]:
                    sum += numbers_table[j][0]
                    if reminder<numbers_table[j][0]:
                        sum-=reminder*2
                    reminder =numbers_table[j][0]
    print(sum)




















number_recognizer(str(input("Enter your number:")))
