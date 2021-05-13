import networkx as nx
from networkx import DiGraph
import sys
import time
from typing import Tuple

global MAXN, INF
MAXN = 100; # max amount of vertex
INF = 100001; # infinity consttant

def bfs(graph: DiGraph, G_F: DiGraph, n: int, s: int, t: int) -> bool: #bfs algorithm
	queue = [s]
	global levels
	levels = [-1] * n
	levels[s] = 0
	level = 0
	while(len(queue) != 0):
		currentV = queue.pop(0)
		for edge in G_F.edges(currentV):
			if(G_F[currentV][edge[1]]['weight'] > 0 and levels[edge[1]] == -1):
				levels[edge[1]] = levels[currentV] + 1
				queue.append(edge[1])
			if(levels[t] > 0):
				return True
	return levels[t] > 0
			

def dfs(graph: DiGraph, G_F: DiGraph, k: int, m: float) -> float: #bfs algorithm
	tmp = m
	if(not m):
		return 0
	if k == len(graph) - 1:
		return m
	for edge in G_F.edges(k):
		to = edge[1]
		if (levels[to] == levels[k] + 1) and (G_F[k][to]['weight'] > 0):
			f = dfs(graph,G_F,to,min(tmp, G_F[k][to]['weight']))
			G_F[k][to]['weight'] = G_F[k][to]['weight'] - f
			if G_F.has_edge(to, k):
				G_F[to][k]['weight'] = G_F[to][k]['weight'] + f
			else:
				G_F.add_edge(to, k, weight=f)
			tmp = tmp - f
	return m - tmp
	
def MaxFlow(graph: DiGraph, s: int, t: int) -> Tuple[float, DiGraph]: #algorithm of searching maxflow
    n = len(graph)
    G_F = graph.copy()
    flow = 0
    while(bfs(graph,G_F, n, s, t)):
    	flow = flow + dfs(graph,G_F,s, INF)
    return flow, G_F


if __name__ == '__main__':
    files = ['test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt', 'test_6.txt', 
            'test_d1.txt', 'test_d2.txt', 'test_d3.txt', 'test_d4.txt', 'test_d5.txt', 
            'test_rd01.txt', 'test_rd02.txt', 'test_rd03.txt', 'test_rd04.txt',
            'test_rl01.txt', 'test_rl02.txt', 'test_rl03.txt', 'test_rl04.txt', 'test_rl05.txt',
            'test_rl06.txt', 'test_rl07.txt', 'test_rl08.txt', 'test_rl09.txt', 'test_rl10.txt']

    #exit limit of time: test_rd05.txt, test_rd06.txt, test_rd07.txt

    sys.setrecursionlimit(1500)

    for fname in files:
        path = './Test/'
        with open(path + fname, "r") as f:
            n, m = map(int, f.readline().split(' '))
            graph = nx.DiGraph()
            for line in f:
                a, b, c = map(int, line.split(' '))
                graph.add_edge(a-1, b-1, weight=c)
            s, t = 0, n - 1

            start = time.time()
            print(str(files.index(fname)) + "." + fname + ":")
            a = MaxFlow(graph, s, t)
            print("\tMax flow: ", a[0])
            print("\t%s seconds" % (time.time() - start))

#a - 1 and b - 1
# 4 5
# 1 2 10000
# 1 3 10000
# 2 3 1
# 3 4 10000
# 2 4 10000


#---a b----
# 6 9
# 0 1 10
# 0 2 10
# 1 2 2
# 1 4 8
# 1 3 4
# 2 4 9
# 3 5 10
# 4 3 6
# 4 5 10