import heapq
from collections import defaultdict

from classes import GraphNode, Graph

def recommend(anime:list[GraphNode], graph):
    n = len(anime)
    potential_recs = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):
            path = dijkstra(anime[i], anime[j], graph)
            if not path:
                continue
            for ani in path:
                if ani in anime:
                    continue
                potential_recs[ani] += 1/len(path)
    
    recs = sorted([(mid_count, ani) for ani, mid_count in potential_recs.items()], key=lambda x: x[0])

    return [rec[1] for rec in recs][:3]


def dijkstra(start:GraphNode, end:GraphNode, graph:Graph, cache=None):    
    if cache is None:
        cache = {}

    cache_key = (start, end)
    if cache_key in cache:
        return cache[cache_key]
    
    counter = 0
    queue = [(0, counter, start)]
    visited = set()
    best_dists = {start: 0}
    prevs = {start: None}

    while queue:
        dist, _, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            break
        for neighbour, weight in node.get_neighbours(graph):
            if neighbour in visited:
                continue
            new_dist = dist + weight
            counter += 1
            if neighbour not in best_dists or new_dist < best_dists[neighbour]:
                best_dists[neighbour] = new_dist
                prevs[neighbour] = node
                heapq.heappush(queue, (new_dist, counter, neighbour))
        print("getting perfect recommendations...")

    shortest_path = []
    curr_node = end

    if curr_node not in prevs:
        cache[cache_key] = []
        return []
    
    while curr_node is not None:
        shortest_path.append(curr_node)
        curr_node = prevs[curr_node]

    cache[cache_key] = shortest_path[len(shortest_path):0:-1]

    return cache[cache_key]