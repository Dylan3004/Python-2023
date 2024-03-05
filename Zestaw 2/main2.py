
def analize (sentence):
    word_counter = 0
    letters="QABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz1234567890"
    letters_counter=[0]*len(letters)
    #print(len(letters_counter))

    start = 0
    while sentence!="":
        sentence = letter_finder(sentence)
        if sentence=="":
            break
        sentence,letters_counter = void_finder(sentence,letters,letters_counter)
        word_counter+=1

    for i in range(len(letters_counter)):
        if letters_counter[i]!=0:
            print("Letter",str(letters[i]),"is in",str(letters_counter[i]),"places, which is ",end="")
            print(str('{:.{prec}f}'.format(letters_counter[i]/len(letters_counter)*100,prec=4)),end="")
            print("% of whole word")
    return word_counter,letters_counter



def letter_finder(sentence):
    start = 0
    for i in range (len(sentence)):
        if sentence[i]!=" ":
            break
        else:
            start+=1
    #print(start)
    sentence = sentence[start:]
    #print(sentence)
    return sentence

def void_finder(sentence,letters,letters_counter):
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            break
        else:
            if sentence[i] in letters:
                #print(str(letters).index(sentence[i]))
                #print(len(letters_counter))
                letters_counter[str(letters).index(sentence[i])]+=1
            start += 1
    sentence = sentence[start:]
    #print(sentence)
    return sentence,letters_counter

print(analize("0ala ma kota MIECIUUUUU      sigma wdd  dwefwef   w f f f f "))
your_own = str(input("Enter a string:"))
analize(your_own)
