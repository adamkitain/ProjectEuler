lookup = {
    1: [1]
}
def collatz_recur(n):
    if n in lookup:
        return lookup[n]
    if n % 2 == 1:
        chain = collatz_recur(3 * n + 1)
        lookup[n] = chain
        return [n] + chain
    else:
        chain = collatz_recur(n / 2)
        lookup[n] = chain
        return [n] + chain

max_len = 0
record = 0
for i in range(1,1000000):
    chain = collatz_recur(i)
    lookup[i] = chain
    if len(chain) > max_len:
        max_len = len(chain)
        record = i

print record, max_len