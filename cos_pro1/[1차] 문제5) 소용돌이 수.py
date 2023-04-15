"""
< 문제 >
    소용돌이 수

< 문제 설명 >
    다음과 같이 n x n 크기의 격자에 1부터 n x n까지의 수가 하나씩 있습니다.
    이때 수가 다음과 같은 순서로 배치되어있다면 이것을 n-소용돌이 수라고 부릅니다.
    소용돌이 수에서 1행 1열부터 n 행 n 열까지 대각선상에 존재하는 수들의 합을 구해야 합니다.
    위의 예에서 대각선상에 존재하는 수의 합은 15입니다.
    격자의 크기 n이 주어질 때 n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    격자의 크기 n이 solution 함수의 매개변수로 주어집니다.
    n은 1 이상 100 이하의 자연수입니다.

< return 값 설명 >
    n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 해주세요.
"""

def solution(n):
    # 1. [n * n]개의 소용돌이 - 2차원 리스트를 제작한다.
    a = [ [0]* n for _ in range(n)] # [0]으로 가득찬 [n * n] 2차원 리스트 생성

    dir = 0                         # 소용돌이 방향 (0 1 2 3 0 1 2 3 ...)
    loop = n                        # 해당 방향으로 채우는 숫자 개수 (ex. 5 4 4 3 3 2 2 1 1)

    r, c = 0, -1                    # 좌표의 초기 값 (row, column)
    dr = [0, 1, 0, -1]              # 방향에 대한 r의 변량
    dc = [1, 0, -1, 0]              # 방향에 대한 c의 변량

    # 2. 빈 2차원 리스트에 소용돌이 형태로 숫자를 채워 넣는다.
    num = 0
    while num < n * n :             # (n * n) 크기의 2차원 배열이 꽉 찰 때까지 진행.-
        for _ in range(loop):       # n번 만큼 반복
            r += dr[dir]            # row 값을 누적함, dr[dir] => 0, 1, 0, -1를 순차적으로 누적함
            c += dc[dir]            # column 값을 누적함, dc[dir] => 1, 0, -1, 0을 순차적으로 누적함
            num += 1                # 배열의 요소 값을 카운트
            a[r][c] = num           # 누적된 r 값과 c 값을 2차우너 리스트의 위치로 사용함 => 그 후, num을 누적함

        dir = (dir + 1) % 4         # 방향 값이 3 => 4로 변함 => 3이 되기 전까지는 0,1,2을 반환

        if dir % 2 :                # 소용돌이 수는 2번씩 동일한 값으로 반복하며 요소를 추가함
            loop -= 1               # 즉, loop를 1인 경우 1번 감소 3인 경우 1번 감소
                                    # 총 4번 반복 중에 loop 값이 2만큼 감소

    # 3. n-소용돌이 수의 대각선상에 존재하는 수들의 합을 구한다.
    answer = 0
    for x in range(n):
        answer += a[x][x]           # 대각선은 항상 row와 col 값이 동일함 => answer[x][x]에 접근하여 값 누적
    return answer


n1 = 3
ret1 = solution(n1)
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)
print("solution 함수의 반환 값은", ret2, "입니다.")