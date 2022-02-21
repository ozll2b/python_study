n=int(input())

def pattern(n):
    if n==3:
        return ['***','* *','***']
    else:
        result=[]
        pre_n=n//3
        pp=pattern(pre_n)
        for i in range(n):
            if pre_n<=i<pre_n*2:
                result.append(pp[i%pre_n]+' '*pre_n+pp[i%pre_n])
            else:
                result.append(pp[i%pre_n]*3)
    return result

for p in pattern(n):
    print(p)
