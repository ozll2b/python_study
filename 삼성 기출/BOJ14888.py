# from itertools import permutations
# from collections import deque
# n=int(input())
# arr=list(map(int,input().split()))
# op_cnt=list(map(int,input().split()))
# op=['+','-','*','/']
# op_list=[]
# for o,c in zip(op,op_cnt):
#     op_list += [o]*c
# opp=list(set(permutations(op_list)))
#
# def cal(a,b,o):
#     if o=='+':
#         return a+b
#     if o=='-':
#         return a-b
#     if o=='*':
#         return a*b
#     if o=='/':
#         return int(a/b)
# result=[]
# for l in opp:
#     numbers=deque(arr)
#     for o in l:
#         a=numbers.popleft()
#         b=numbers[0]
#         numbers[0]=cal(a,b,o)
#     result.append(numbers[0])
# print(max(result))
# print(min(result))


import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)