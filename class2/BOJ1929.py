m,n=map(int,input().split())

array = [True for i in range(n + 1)]


for i in range(2, int(n**0.5) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

prime=[x for x in range(len(array)) if array[x] and x>=m and x!=1]

for num in prime:
    print(num)