from itertools import product
from copy import deepcopy
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]


def left(board):
    result=[]
    for arr in board:
        if sum(arr)==0:
            result.append([0]*len(board))
            continue
        arr=[x for x in arr if x!=0]
        stack=[]
        pre=arr[0]
        stack.append(arr.pop(0))
        while arr:
            if pre==arr[0] and arr[0]==stack[-1]:
                stack[-1]*=2
            else:
                stack.append(arr[0])
            pre=arr.pop(0)
        if len(stack)<len(board): stack+=[0]*(len(board)-len(stack))
        result.append(stack)
    return result

def right(board):
    result = []
    for arr in board:
        if sum(arr)==0:
            result.append([0]*len(board))
            continue
        arr = [x for x in arr if x != 0]
        arr.reverse()
        stack = []
        pre = arr[0]
        stack.append(arr.pop(0))
        while arr:
            if pre == arr[0] and arr[0] == stack[-1]:
                stack[-1] *= 2
            else:
                stack.append(arr[0])
            pre = arr.pop(0)
        stack.reverse()
        if len(stack) < len(board): stack = [0] * (len(board) - len(stack)) +stack
        result.append(stack)
    return result


def up(board):
    result=[[0]*len(board) for _ in range(len(board))]
    for j in range(len(board)):
        arr=[]
        sum=0
        for i in range(len(board)):
            if board[i][j]:
                arr.append(board[i][j])
                sum += board[i][j]
        if sum:
            stack = []
            pre = arr[0]
            stack.append(arr.pop(0))
            while arr:
                if pre == arr[0] and arr[0] == stack[-1]:
                    stack[-1] *= 2
                else:
                    stack.append(arr[0])
                pre = arr.pop(0)
            for k in range(len(stack)):
                result[k][j]=stack[k]
    return result

def down(board):
    result=[[0]*len(board) for _ in range(len(board))]
    for j in range(len(board)):
        arr = []
        sum = 0
        for i in range(len(board)):
            if board[i][j]:
                arr.append(board[i][j])
                sum += board[i][j]
        arr.reverse()
        if sum:
            stack = []
            pre = arr[0]
            stack.append(arr.pop(0))
            while arr:
                if pre == arr[0] and arr[0] == stack[-1]:
                    stack[-1] *= 2
                else:
                    stack.append(arr[0])
                pre = arr.pop(0)

            k=len(board)-1
            l=0
            while l<len(stack):
                result[k][j]=stack[l]
                k -=1
                l +=1

    return result

def find_max(board):
    m=0
    for numbers in board:
        m=max(m,max(numbers))
    return m


def move(board,o):
    if o == 0:
        board = up(board)
    elif o == 1:
        board = down(board)
    elif o == 2:
        board = right(board)
    elif o == 3:
        board= left(board)
    return board

def dfs(board, cnt):
    global ans
    if cnt == 5:
        ans = max(ans, find_max(board))
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

ans = 0
dfs(board, 0)
print(ans)