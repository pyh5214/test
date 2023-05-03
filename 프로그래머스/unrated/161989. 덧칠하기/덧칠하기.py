def solution(n, m, section):
    section.sort()  # 다시 칠해야 할 구역을 정렬합니다.
    count = 0  # 롤러를 사용한 횟수를 저장할 변수입니다.
    current_pos = 0  # 롤러의 현재 위치를 저장할 변수입니다.
    
    for sec in section:
        # 다시 칠해야 할 구역의 왼쪽 끝부터 시작합니다.
        if sec <= current_pos:
            continue
        
        # 다시 칠해야 할 구역의 왼쪽 끝으로 롤러를 이동합니다.
        count += 1
        current_pos = sec - 1
        
        # 롤러를 구역의 오른쪽 끝 또는 벽의 오른쪽 끝까지 이동시키면서 벽을 칠합니다.
        right_end = min(current_pos + m, n)
        current_pos = right_end
        if right_end == n:
            break
    
    return count
