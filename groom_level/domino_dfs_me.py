# -*- coding: utf-8 -*-

def get_domino(graph, v, visited, dom = 1):
	visited[v-1] = True
	for i in graph[v-1]:
		if not visited[i-1]:
			get_domino(graph, i, visited,dom)


a,b,c = map(int, input().split())
visited = [False] * a
graph = []
for i in range(a):
	graph.append([])
	
for i in range(b):
	start, end = map(int, input().split())
	graph[start-1].append(end)

fall = 0
for i in range(c):
	pushed = int(input())
	visited = [False] * a
	visited[pushed-1]=True
	get_domino(graph, pushed, visited)
	for k in range(a):
		if visited[k]==True:
			fall += 1
	
print(fall)

