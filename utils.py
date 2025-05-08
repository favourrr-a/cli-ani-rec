import pickle
import csv
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
            anime = Anime(row[0], set(row[1:]))
            anime_list.append(anime)
    return anime_list

def create_anime_graph(anime_file, graph_name):
    anime_list = csv_to_list(anime_file)

    anime_nodes = [GraphNode(anime) for anime in anime_list]

    for anime_node in anime_nodes:
        anime_node.add_neighbours(anime_nodes)

    anime_graph = Graph(anime_nodes)
    save_object(anime_graph, graph_name)
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