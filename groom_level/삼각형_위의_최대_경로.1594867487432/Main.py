from collections import deque

def get_path(x,y):
	queue = deque()
	queue.append((x,y))
	
	while queue:
		x, y = queue.popleft()
	
		for i in range(2):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx >= n or ny > len(tri[nx]):
				continue
				
			if path_val[nx][ny] < path_val[x][y] + tri[nx][ny]:
				path_val[nx][ny] = path_val[x][y] + tri[nx][ny]
			queue.append((nx,ny))

n=int(input())
tri=[[int(x) for x in input().strip().split(" ")] for j in range(n)]
dx = [1, 1]
dy = [0, 1]
path_val = []
for i in range(n):
	path_val.append([])
	for j in range(n):
		path_val[i].append(-1)
	
path_val[0][0] = tri[0][0]
get_path(0,0)
print(max(path_val[n-1]))

