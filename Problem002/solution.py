def get_fib(a, b):
    if b < 4000000:
        return [a] + get_fib(b, a+b)
    else:
        return [a, b]

full_fib = get_fib(1, 1)
even_fib = [f for f in full_fib if ~f % 2]
print sum(even_fib)