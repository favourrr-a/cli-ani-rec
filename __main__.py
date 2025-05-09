from utils import output_anime, anime_to_nodes, load_object, get_info, get_valid_titles, create_anime_graph
from rec_algo import recommend

anime_graph = load_object("anime_graph_updated.pickle")
valid_titles = get_valid_titles(anime_graph)

def main():
    titles = get_info(valid_titles)
    nodes = anime_to_nodes(titles, anime_graph)
    return output_anime(recommend(nodes, anime_graph))    

if __name__ == '__main__':
    print(main())