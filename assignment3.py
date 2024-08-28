def remove (lst, num):
    while num in lst:
        lst.remove(num)
    return lst
print(remove([1, 2, 3, 4, 2, 5, 2],2))
print(remove([5, 5, 5, 5, 5],5))
print(remove([1, 2, 3, 4, 5] ,0 )) 