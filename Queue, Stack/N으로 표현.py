def solution(N, number):
    # 인덱스가 N을 몇 번 사용했는지를 나타냄 ex) dp_table[1]: 1번 사용, d_table[4]: 4번 사용
    dp_table = [[]]
    for i in range(1, 9):  # N 조건이자 사용 횟수 조건(8보다 크면 -1 리턴)
        case = []
        for j in range(1, i):
            for k in dp_table[j]:  # j번 사용한 경우의 수 원소 iteration
                for l in dp_table[i - j]:  # i-j번 사용한 경우의 수 원소 iteration
                    case.append(k + l)  # 더하기
                    if k - l >= 0:
                        case.append(k - l)  # 빼기
                    case.append(k * l)  # 곱하기
                    if l != 0 and k != 0:
                        case.append(k // l)  # 나누기
        case.append(int(str(N) * i))  # 숫자를 그대로 이어 붙인 케이스 ex) 55, 555

        if number in case:
            return i
        dp_table.append(list(set(case)))
    return -1