import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
ground = []

for i in range(n):
    ground.append(list(map(int, input().split())))

mt, hl = int(1e9), 0

for level in range(257):
    t = 0
    lower, higher = 0, 0
    for i in range(n):
        lower += sum([level - x for x in ground[i] if x < level])
        higher += sum([x - level for x in ground[i] if x > level])

    if b + higher - lower < 0:
        break

    t += (2 * higher + 1 * lower)
    if t <= mt or higher + lower == 0:
        mt = t
        hl = level

print(mt, hl)