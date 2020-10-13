def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))