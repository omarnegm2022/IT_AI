def all_even(start: int, end: int):
    for i in range(start, end+1):
        if not i%2:
            yield i

print(*all_even(1,16))
        