def summation(n1:int, n2: int, n3: int):
    if (n1 == n2) or (n2 == n3) or (n1 == n3):
        return 0
    return (n1 + n2 + n3)

print(summation(*([int(i) for i in input("Enter the 3, integer, numbers. Separated by a space: ").split()])))