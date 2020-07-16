from collections import deque

def check_path(x, y):
	queue = deque()
	queue.append((x,y))
	
	while queue:
		x,y=queue.popleft()
		cVal = board[x][y]
		
		for i in range(2):
			if i%2==0:
				nx = x
				ny = y + cVal
			else:
				nx = x + cVal
				ny = y
			
			if nx >= 7 or ny >=7:
				continue
			
			if possible[nx][ny]==0:
				possible[nx][ny]=1
				queue.append((nx,ny))
	
board=[[int(i) for i in input().strip().split(' ')]for j in range(7)]

possible=[]
for i in range(7):
	possible.append([])
	for j in range(7):
		possible[i].append(0)
		
possible[0][0] = 1
check_path(0,0)

print(possible[6][6])

