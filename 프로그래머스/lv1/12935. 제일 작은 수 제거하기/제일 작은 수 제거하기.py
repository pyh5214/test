def solution(arr):
    if len(arr) <= 1:
        answer = []
        answer.append(-1)
        return answer
    else:
        arr.remove(min(arr))
        return arr