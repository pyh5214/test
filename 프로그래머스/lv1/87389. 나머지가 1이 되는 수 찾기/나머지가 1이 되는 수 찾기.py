def solution(n):
    xlist = []
    for i in range(2,n):
        if n%i == 1:
            xlist.append(i)
    x = min(xlist)
    answer = x
    return answer