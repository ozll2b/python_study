import sys

s=sys.stdin.readline().rstrip().split('-')
result=0

result += sum(list(map(int,s.pop(0).split('+'))))
for i in range(len(s)):
    result -= sum(list(map(int,s[i].split('+'))))
print(result)
