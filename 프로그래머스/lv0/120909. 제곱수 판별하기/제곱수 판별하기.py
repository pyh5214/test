def solution(n):
    a = n**(1/2)
    if int(a) == a:
        answer = 1
    else:
        answer = 2
    return answer