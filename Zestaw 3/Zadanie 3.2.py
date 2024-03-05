def odwracanie(L,left,right):
    for i in range((right+1-left)//2):
        print(L[left+i])
        print(L[right-i])
        temp=L[left+i]
        L[left+i]=L[right-i]
        L[right-i]=temp
    return L

def odwracanie_rec(L,left,right,left_list,right_list):
    if(right>left):
        left+=1
        right-=1
        print(left,right)
        left_list.append(L[left-1])
        right_list.append(L[right+1])
        print(left_list)
        print(right_list)
        odwracanie_rec(L,left,right,left_list,right_list)
    else:
        if left == right :
            L[left-len(left_list):left]= right_list
            L[left+1 :left + len(left_list)+1] = left_list[::-1]
        else:
            L[left - len(left_list):left] = right_list
            L[left:left + len(left_list)] = left_list[::-1]

    return L


List = [1, 2, 3, 4, 5, 6, 7]
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

# for i in range(len(List)-1):
#     for j in range(len(List)-1):
#         print("Odwracanie jako ",i,j)
#         print(odwracanie(List,i,j))

print(odwracanie(List,0,2))

print(odwracanie_rec(List1,1,8,[],[]))

