def solution(s):
    list_ = list(map(int, s.split( )))
    print(list_)
    aa = "{0} {1}".format(min(list_),max(list_))
    return aa