numbers = [2, 4, 6, 8, 7, 10]
def find_odd(numbers):
    evens = sum(1 for n in numbers if n % 2 == 0)
    odds = len(numbers) - evens

    if evens > odds:
        return next (n for n in numbers if n % 2 != 0)
    else:
        return next (n for n in numbers if n % 2 == 0)
print(find_odd(numbers))