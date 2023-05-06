def n_queen(n):
    count = 0
    cols = [-1] * n  # 퀸이 놓인 열을 저장하는 리스트
    
    # 대각선 방향에 이미 퀸이 있는지 검사하는 함수
    def is_available(row, col):
        for i in range(row):
            if cols[i] == col or abs(cols[i] - col) == row - i:
                return False
        return True
    
    # 가지치기 기법을 사용하여 퀸을 놓는 함수
    def place_queen(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col not in cols and all(abs(col - cols[i]) != row - i for i in range(row)):
                cols[row] = col
                place_queen(row + 1)
                cols[row] = -1
    
    # 첫 번째 열부터 탐색 시작
    place_queen(0)
    return count

n = int(input())
print(n_queen(n))
