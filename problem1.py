number = 18

sum_of_digits = lambda n: sum(int(digit) for digit in str(n) if digit.isdigit())
result = sum_of_digits(number)
print(result)