
def raise_power(numbers, n):
    powered_nums = list(map(lambda x: x**n, numbers))
    return powered_nums

numbers = [1, 2, 3, 4, 5]
n = 5
powered_nums = raise_power(numbers, n)
print(powered_nums)