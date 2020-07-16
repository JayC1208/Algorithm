def get_tile(n):
	if n==1:
		tiles[n] = 1
		return 1
	if n==2:
		tiles[n] = 2
		return 2
	
	if tiles[n]==-1:
		tiles[n]=get_tile(n-1)+get_tile(n-2)
		
	return tiles[n]
	
	
	
k = int(input())
tiles = [-1]*(k+1)
if k%2==0:
	print(get_tile(k)-tiles[k//2] - tiles[k//2-1])
else:
	print(get_tile(k)-tiles[k//2])
