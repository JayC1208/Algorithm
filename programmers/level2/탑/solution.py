def solution(heights):    
    answer = []
    tot = len(heights)
    for m in range(0,tot):
        me = heights.pop()
        flag = 0
        for i, x in enumerate(list(reversed(heights))):
            if x > me:
                answer.append(tot-1 - m -i)
                flag = 1
                break
        if not flag:
            answer.append(0)
            
    return list(reversed(answer))
