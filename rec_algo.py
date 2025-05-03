import heapq

from classes import GraphNode

def recommend(anime:list[GraphNode]):
    potential_recs = []

    if len(anime) == 1:
        for neighbour in anime[0].neighbours:
            potential_recs.append((neighbour, anime[0].neighbours[neighbour]))
    else:
        paths_between = []
        for i in range(len(anime)):
            for j in range(i, len(anime)):
                paths_between.append((anime[i], anime[j]))  
        for start, end in paths_between:
            potential_recs.append(dijkstra(start, end))  

    recs = heapq.nsmallest(3, potential_recs, key = lambda x: x[1])
    sorted_recs = sorted(recs, key = lambda x: x[1])

    return [rec[0] for rec in sorted_recs]

def dijkstra(start:GraphNode, end:GraphNode):
    shortest_path = []

    return shortest_path

