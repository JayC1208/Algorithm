def solution(prices):
    answer = []
    for i in range(len(prices)):
        me = prices[i]
        cnt = 0
        for j in range(i+1, len(prices)):
            now = prices[j]
            cnt += 1
            if now >= me:
                pass
            else:
                break
        answer.append(cnt)
    return answer
