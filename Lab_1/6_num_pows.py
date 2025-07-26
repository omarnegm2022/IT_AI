# def numbs(i):
#     yield i**2

# print(*(list(numbs())))
print(*[i**2 for i in range(1, 17)])