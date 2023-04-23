def solution(name, yearning, photo):
    result = []
    for p in photo:
        point = 0
        for i in p:
            if i in name:
                point += yearning[name.index(i)]
        result.append(point)
    return result