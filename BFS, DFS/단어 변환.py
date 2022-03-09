def solution(begin, target, words):
    answer = 0
    visited=[False]*len(words)
    if target in words:
        for i in range(len(words)):
            if begin==target:
                break
            else:
                begin=dfs(begin,target,words,i,visited)
                answer += 1
    return answer

def dfs(begin,target,words,v,visited):
    if len(set(begin) - set(target)) == 1:
        return target
    if not visited[v] and len(set(begin) - set(words[v])) == 1:
        visited[v]==True
        return words[v]
    else:
        return begin

