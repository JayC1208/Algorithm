
a,b,c = map(int,input().split())

graph=[[] for _ in range(a+1)]
visited = [[False]*(a+1)]

for _ in range(b):
    x,y = map(int, input().split())
    graph[x].append(y)

result = 0

def dfs(v):
    global result
    if visited[v]:
        return
    vistied[v]=True
    result+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)



for _ in range(c):
    v = int(input())
    dfs(v)

print(result)
