def second_largest(lst):
    lst = list(lst)
    lst.sort(reverse=True)
    return lst[1]

print(second_largest([1,2,3,6,5,5]))
