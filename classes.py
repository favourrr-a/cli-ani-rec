from __future__ import annotations
from collections import deque

class Anime:
    def __init__(self, title, genres):
        self.title = title
        self.genres = genres

class GraphNode:
    
    def __init__(self, anime:Anime):
        self.anime = anime
        self.neighbours = {}
        ## {neighbour: weight}

    def add_neighbours(self, neighbours:list[GraphNode]):
        n = len(self.anime.genres)
        for neighbour in neighbours:
            if self.anime == neighbour.anime:
                continue
            common_genres = len(self.anime.genres.intersection(neighbour.anime.genres))
            if common_genres != 0:
                self.neighbours[neighbour] = n - common_genres 
        
class Graph:
    def __init__(self, nodes:list[GraphNode]):
        self.nodes = nodes
    def remove_nodes(self, nodes:list[GraphNode]):
        return
    def add_nodes(self, node:list[GraphNode]):
        return
    def display(self):
        visited = set()
        queue = deque([self.nodes[0]])

        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbour in current_node.neighbours:
                queue.append(neighbour)
            print(current_node.anime.title)
        
        for node in self.nodes:
            if node not in visited:
                print(node.anime.title)