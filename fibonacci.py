def fibonacci(num):
    if num < 0:
        raise Exception('Number must be positive.')
    arr = []
    for n in range(num):
        if len(arr) >= 2:
            arr.append(sum(arr[-2:]))
        else:
            arr.append(1)
    return arr

print(fibonacci(10))
