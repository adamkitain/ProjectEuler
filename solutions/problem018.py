import time

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

with open('data/p067_triangle.txt', 'r') as f:
    triangle = f.read()
triangle = triangle.split('\n')
triangle = triangle[:100]
triangle = [[int(x) for x in t.split(' ')] for t in triangle]

lookup = {}
# triangle = [
# [3],
# [7,4],
# [2,4,6],
# [8,5,9,3],
# ]

def traverse_down(down, i):
    global lookup
    key = str(down) + str(i)
    if key in lookup:
        return lookup[key]
    if len(down) == 1:
        try:
            return down[0][i]
        except:
            return 0
    down_sum = down[0][i] + max(traverse_down(down[1:], i), traverse_down(down[1:], i+1))
    lookup[key] = down_sum
    return down_sum

def choose_above(d, i):
    global triangle
    if d == 0:
        return triangle[0][0]
    if i >= len(triangle[d]):
        return 0
    right = choose_above(d - 1, i)
    if i == 0:
        return triangle[d][i] + right
    left = choose_above(d-1, i-1)
    if right > left:
        return triangle[d][i] + right
    else:
        return triangle[d][i] + left

depth = len(triangle)
t0 = time.time()
print traverse_down(triangle, 0)
t1 = time.time()
best_path = 0
for i in range(depth):
    path_sum = choose_above(depth-1, i)
    best_path = max(path_sum, best_path)
t2 = time.time()

print best_path
print "1: ", (t1-t0)
print "2: ", (t2-t1)
