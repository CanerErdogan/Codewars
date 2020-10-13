values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

numbers = ['MCMXC', 'MMVIII', 'MDCLXVI']

def solution(roman):
    decimal = 0
    for i in range(len(roman)-1):
        if (value := values[roman[i]]) >= values[roman[i+1]]:
            decimal += value
        else:
            decimal -= value
    return decimal + values[roman[-1]]

for n in numbers: print(solution(n))