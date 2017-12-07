import heapq
import sys
import pandas as pd
import ast
import urllib2
from coordinates_nodes import *
#from kshort import *
class Graph():
	
	def __init__(self):
		self.vertices = {}

	def add_vertex(self,edges):
		self.vertices = edges
	
	def shortest_path(self,start,end):
		distance = {}
		parent ={}
		node = []
		visited = {}
		for v in self.vertices:

			if v == start:
				distance[v] = 0
				visited[v] = 0
				heapq.heappush(node,[0,v])	
			else:
				distance[v] = sys.maxsize
				visited[v] = 0
				heapq.heappush(node,[sys.maxsize,v])
			parent[v] = None				
		
		while node:
			small = heapq.heappop(node)[1]
			if small == end:
				path =[]
				while parent[small]:
					path.append(small)
					small = parent[small]
				return path,distance
		
			for n in self.vertices[small]:
				if visited[n] !=1:
					alt = distance[small] + self.vertices[small][n]
					if alt < distance[n]:
						distance[n] = alt
						parent[n] = small
						visited[n] = 1
						for k in node:
                        				if k[1] == n:
                            					k[0] = alt
                            					break
                    				heapq.heapify(node)

		return distance

def publish(temp,temp1):
        url = "https://ironmaniiits.pythonanywhere.com/BTP/default/fun3/" + str(temp) +"/"+str(temp1)+"/"
        print url
        result = urllib2.urlopen(url).read() 




if __name__=='__main__':
    g = Graph()
    with open('node_edge_netwrok.txt','r') as txt:
	r = txt.read()
    d = ast.literal_eval(r)
    g.add_vertex(d)
    n=input()
    m=input()
    #s=input()
    #t,x = ksp_yen(g,n,m)
    k,l =  g.shortest_path(n,m)
    publish(-1,-1)
    for i in k:
	print  i,l[i],coordinates[i][0],coordinates[i][1]
        publish(coordinates[i][1],coordinates[i][0])
    #for i in t:
     #    print  i,x[i],coordinates[i][0],coordinates[i][1]
