from __future__ import annotations
from collections import deque
import heapq

class Anime:
    def __init__(self, title, genres):
        self.title = title
        self.genres = genres

class GraphNode:
    def __init__(self, anime:Anime):
        self.anime = anime
        self.neighbours = {}
        ## {neighbour: weight}

    def add_neighbours(self, potential_neighbours:list[GraphNode]):
        similar_anime = []

        for potential in potential_neighbours:
            if self.anime == potential.anime:
                continue
            total_genres = len(self.anime.genres.union(potential.anime.genres))
            common_genres = len(self.anime.genres.intersection(potential.anime.genres))
            if common_genres == 0:
                continue
            weight = common_genres / total_genres
            if weight >= 0.05:
                similar_anime.append((potential, weight))

        if len(similar_anime) != 0:
            similar_anime = heapq.nlargest(10, similar_anime, key = lambda x: x[1])
            
        self.neighbours = {node.anime.title: weight for node, weight in similar_anime}
    
    def get_neighbours(self, graph:Graph):
        neighbours = []
        for n in self.neighbours.keys():
            neighbours.append((graph.nodes[n.lower()], self.neighbours[n]))
        return neighbours
        
class Graph:
    def __init__(self, nodes:list[GraphNode]):
        self.nodes = {}
        for node in nodes:
            self.nodes[node.anime.title.lower()] = node

    def remove_nodes(self, nodes:list[GraphNode]):
        return
    def add_nodes(self, node:list[GraphNode]):
        return
    
    def get_node(self, title:str):
        return self.nodes[title.lower()]
    
    def display(self):
        nodes = list(self.nodes.values())
        visited = set()
        queue = deque([nodes[0]])

        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbour in current_node.neighbours:
                queue.append(neighbour)
            print(current_node.anime.title)
        
        for node in nodes:
            if node not in visited:
                print(node.anime.title)