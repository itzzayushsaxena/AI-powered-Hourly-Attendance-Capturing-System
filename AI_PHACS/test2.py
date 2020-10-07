def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


t1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List Before Sorting:\n", t1)
print("List After Sorting:\n", Sort_Tuple(t1))
