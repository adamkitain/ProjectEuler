def is_palindrome(x):
    x1 = str(x)
    x2 = ''.join([x1[i] for i in range(len(x1)-1,-1,-1)])
    return x1 == x2

multiples = []
for i in range(100,999):
    for j in range(100,999):
        multiples.append(i*j)

print max([m for m in multiples if is_palindrome(m)])