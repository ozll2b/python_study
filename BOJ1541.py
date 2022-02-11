import sys

s=sys.stdin.readline().rstrip()
result=0
s = s.split('-')
result += sum(list(map(int,s.pop(0).split('+'))))
for i in range(len(s)):
    result -= sum(list(map(int,s[i].split('+'))))
print(result)
