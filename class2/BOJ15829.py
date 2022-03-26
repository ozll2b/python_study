dic={}
alpha=[chr(i) for i in range(ord('a'),ord('z')+1)]
for i in range(1,27):
    dic[alpha[i-1]]=i

l=int(input())
s=input()
result=0
for i in range(l):
    result += dic[s[i]]*(31**i)
print(result%1234567891)