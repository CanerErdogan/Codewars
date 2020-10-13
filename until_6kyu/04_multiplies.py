def solution(number):
    return sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, list(range(3, number))))


print(solution(10))
