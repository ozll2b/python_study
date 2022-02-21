def solution(routes):
    stack=[]
    routes.sort(key=lambda x:(x[0],x[1]))
    for route in routes:
        if stack and stack[-1][0]<=route[0]<=stack[-1][1]:
            if route[1]<=stack[-1][1]:
                stack.append(route)
                stack.pop(0)
        else:
            stack.append(route)
    return len(stack)