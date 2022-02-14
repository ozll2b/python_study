def solution(name):
    change=[min(ord(i)-ord('A'),ord('Z')-ord(i)+1) for i in name]
    print(sum(change))
    name_left=name[:len(name)//2+1].rstrip('A')
    name_right=name[len(name)//2+1:].lstrip('A')
    right=max(len(name.rstrip('A'))-1,0)
    left=len(name[1:].lstrip('A'))
    right_left=max(len(name_left)-1,0)*2 + len(name_right)
    left_right=len(name_right) * 2 + max(len(name_left) - 1,0)
    print(right,left,left_right,right_left)
    answer = sum(change) + min(right,left,left_right,right_left)
    return answer



print(solution("ZAAAZZZZZZZ"))



