from collections import Counter
n = int(input())

in_list = map(int,input().split())

result = [-1]*n
cnt = 1
prev = -1
bridge = -1

for i, x in enumerate(in_list):
	
	if x > prev:
		result[i] = cnt
	else:
		cnt += 1
		result[i] = bridge
		bridge -=1
		
	prev = x

result[0]=bridge
print(max(Counter(result).values())+1)
