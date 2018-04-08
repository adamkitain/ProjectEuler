words = {
    0: 0, #Never used
    1: 3,   # One
    2: 3,   # Two
    3: 5,   # Three
    4: 4,   # Four
    5: 4,   # Five
    6: 3,   # Six
    7: 5,   # Seven
    8: 5,   # Eight
    9: 4,   # Nine
    10: 3,  # Ten
    11: 6,  # Eleven
    12: 6,  # Twelve
    13: 8,  # Thirteen
    14: 8,  # Fourteen
    15: 7,  # Fifteen
    16: 7,  # Sixteen
    17: 9,  # Seventeen
    18: 8,  # Eighteen
    19: 8,  # Nineteen
    20: 6,  # Twenty
    30: 6,  # Thirty
    40: 5,  # Forty
    50: 5,  # Fifty
    60: 5,  # Sixty
    70: 7,  # Seventy
    80: 6,  # Eighty
    90: 6,  # Ninety
    100: 7  # Hundred
}

def get_score(n):
    if n == 0:
        return 0
    if n <= 20:
        return words[n]
    if n < 100:
        tens = words[n/10*10]
        ones = words[n%10]
        return tens + ones
    else:
        huns = words[n/100]
        rest = get_score(n%100)
        hundred_and = 10
        if n%100 == 0:
            hundred_and = 7
        return huns + hundred_and + rest

run_sum = 0
for i in range(1,1000):
    try:
        run_sum += get_score(i)
    except:
        print i
one_thousand = 11
print run_sum + one_thousand

print get_score(115)