def solution(s, skip, index):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    text = ''
    for i in skip:
        alp = alp.replace(i,"")
        
    alp = alp*3
    
    for j in s:
        num = alp.index(j)
        text += alp[num + index]
    
       
    return text