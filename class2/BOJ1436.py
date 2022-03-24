import sys

n=int(sys.stdin.readline())

result=0
i=0
cnt=0
while cnt<n:
    if '666' in str(i):
        result=i
        cnt +=1
    i +=1

print(result)