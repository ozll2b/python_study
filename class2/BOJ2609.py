
a,b=map(int,input().split())

def gcd(a,b):
    while a and b:
        if a>b:
            a %=b
        else:
            b %=a
    return max(a,b)

def lcm(a,b,gcd):
    return (a*b)//gcd

print(gcd(a,b))
print(lcm(a,b,gcd(a,b)))
