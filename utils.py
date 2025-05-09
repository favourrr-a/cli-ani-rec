import pickle
import csv
import time
from collections import defaultdict
from difflib import get_close_matches
from classes import Anime, GraphNode, Graph

def save_object(obj, file_name:str):
    if not isinstance(file_name, str):
        raise TypeError("Input type must be a string")
    try:
        with open(file_name, "wb") as object_f:
            pickle.dump(obj, object_f)
        object_f.close()
    except Exception as e:
        print("Failed to save object", e)

def load_object(file_name:str):
    if not isinstance(file_name, str):
        raise TypeError("Input type must be a string")
    try:
        with open(file_name, "rb") as object_f:
            return pickle.load(object_f)
    except FileNotFoundError:
        print("Input file not found")
    except Exception as e:
        print("Failed to load object", e)

def csv_to_list(file_name):
    anime_list = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            anime_title = row[1]
            anime_genres = set(row[16].split())
            anime_list.append(Anime(anime_title, anime_genres))
    return anime_list

def create_anime_graph(anime_file, graph_name):
    start_total = time.time()
    start = time.time()
    anime_list = csv_to_list(anime_file)
    print(f"anime list created in {time.time() - start:2f} seconds")

    anime_nodes = [GraphNode(ani) for ani in anime_list]
    start = time.time()
    genre_to_anime = defaultdict(set)
    for ani in anime_nodes:
        for genre in ani.anime.genres:
            genre_to_anime[genre].add(ani)
    print(f"genre to anime map created in {time.time() - start:2f} seconds")

    print("cleaning anime...")
    start = time.time()
    for genre in genre_to_anime.keys():
        new_nodes = set()
        for ani in genre_to_anime[genre]:
            duplicate = False
            for other in genre_to_anime[genre]:
                if ani.anime.title != other.anime.title and ani.anime.title in other.anime.title:
                    duplicate = True
                    break
            if not duplicate:
                print(f"{ani.anime.title} is clean")
                new_nodes.add(ani)
        genre_to_anime[genre] = new_nodes
    print(f"anime cleaned up in {time.time() - start:2f} seconds")

    print("adding neighbours")
    start = time.time()
    for i, anime_node in enumerate(anime_nodes):
        for genre in anime_node.anime.genres:
            anime_node.add_neighbours(list(genre_to_anime[genre]))
        if i % 1000 == 0 and i != 0:
            print(i, "anime processed...")
    print(f"anime neighbours created in {time.time() - start:2f} seconds")

    start = time.time()
    anime_graph = Graph(anime_nodes)
    print(f"anime graph created in {time.time() - start:2f} seconds")

    start = time.time()
    save_object(anime_graph, graph_name)
    print(f"anime graph object saved in {time.time() - start:2f} seconds")
    print(f"total time taken {time.time() - start_total:2f} seconds")

    return graph_name

def get_valid_titles(anime_graph):
    return list(anime_graph.nodes.keys())

def get_info(valid_titles):
    while True:
        input_anime = input('Enter the anime you want recommendations based on:\n').split(',')
        anime = [ani.strip() for ani in input_anime]

        matched_anime = []
        missing_anime = []
        for ani in anime:
            matched = get_close_matches(ani, valid_titles)
            if matched:
                matched_anime.append(matched[0])
            else:
                missing_anime.append(ani)
        if not missing_anime:
            return matched_anime

        print(f"Some anime not found: {(", ").join(missing_anime)}. Retry")

def anime_to_nodes(anime:list[str], anime_graph):
    return [anime_graph.get_node(ani) for ani in anime]

def output_anime(anime:list[GraphNode]):
    return [ani.anime.title for ani in anime]