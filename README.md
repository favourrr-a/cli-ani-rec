# CLI-ANI-REC
Graph-based anime recommender system.

## Overview
- 23k+ anime nodes
- Weighted graph based on similar genres
- Dijkstra for traversal
- Pickled graph object so you don't have to rebuild it (takes 450s to build)

## Limitations
Anime that are direct neighbours (like One Piece and Naruto) will yield an empty recommendation because the shortest path is moving directly from one to the other.

Anime nodes that are far apart will end up having unrelated anime in their recommendations because of how long the path between them is.

Entering more input anime yields results. Although said results are questionable.

## Usage
In \__main__.py, you may switch between using anime_graph.pickle which has only 64 anime or using the 23k+ one, anime_graph_updated.pickle.

This is an expiremental project.