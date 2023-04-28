"""
< 문제 >
    체스의 나이트

< 문제 설명 >
    체스에서 나이트(knight)는 아래 그림과 같이 동그라미로 표시된 8개의 방향중 한 곳으로 한 번에 이동이 가능합니다.
    단, 나이트는 체스판 밖으로는 이동할 수 없습니다.
    체스판의 각 칸의 위치는 다음과 같이 표기합니다.

    예를 들어, A번줄과 1번줄이 겹치는 부분은 'A1'이라고 합니다.
    나이트의 위치 pos가 매개변수로 주어질 때, 나이트를 한 번 움직여서 이동할 수 있는 칸은 몇개인지 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    나이트의 위치 pos가 solution 함수의 매개변수로 주어집니다.
    - pos는 A부터 H까지의 대문자 알파벳 하나와 1 이상 8이하의 정수 하나로 이루어진 두 글자 문자열입니다.
    - 잘못된 위치가 주어지는 경우는 없습니다.

< return 값 설명 >
    나이트를 한 번 움직여서 이동할 수 있는 칸의 개수를 return 해주세요.
"""
def solution(pos):
    """
     [ 유니코드 암기 ]
        - ord('A') : 65
        - ord('a') : 97
        - ord('0') : 48
    """

    r = ord(pos[1]) - ord('1')  # 전달받은 포지션 값 - 아스키 코드(1) 값 => 나이트의 row 값
    c = ord(pos[0]) - ord('A')  # 전달받은 포지션 값 - 아스키 코드(A) 값 => 나이트의 col 값

    dr = [2, 1, -1, -2, -2, -1, 1, 2]  # 나이트의 row 이동 범위 표현
    dc = [1, 2, 2, 1, -1, -2, -2, -1]  # 나이트의 col 이동 범위 표현

    answer = 0

    # 이동 범위의 개수가 8개임
    for i in range(8):
        # 순차적으로 row, col 값 누적함으로써 이동 범위 파악
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < 8 and nc >= 0 and nc < 8: answer += 1
    # 이동 범위(1~8,A~H)를 초과하지 않은 위치에서만 answer 증가
    return answer


pos = "A7"
ret = solution(pos)
print("solution 함수의 반환 값은", ret, "입니다.")