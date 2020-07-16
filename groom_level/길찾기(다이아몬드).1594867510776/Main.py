# -*- coding: utf-8 -*-
from collections import deque
def get_path():
	queue = deque()
	queue.append((0,0))
	
	while queue:
		
		x, y = queue.popleft()
		
		for i in range(2):
			if x>=n-1:
				ny = y+dy_[i]
			else:
				ny=y+dy[i]
			nx = x+dx[i]
			
			if nx >= 2*n -1 or ny >= len(diamond[nx]) or ny <0:
				continue
			# queue.append((nx,ny))
			if path[nx][ny] < path[x][y] + diamond[nx][ny]:
				path[nx][ny] = path[x][y] + diamond[nx][ny]
				queue.append((nx,ny))
	
	
n = int(input())
diamond=[]
path=[]
dx = [1,1]
dy=[0,1]
dy_=[-1,0]
for j in range(2*n-1):
	diamond.append(list(map(int,input().split())))
	path.append([-1]*n)
	

path[0][0] = diamond[0][0]

get_path()
print(path[2*n-2][0])
	
	