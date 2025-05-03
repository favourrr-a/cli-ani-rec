from utils import output_anime, anime_to_nodes, load_object, get_info
from rec_algo import recommend

anime_graph = load_object("anime_graph.pickle")

def main():
    titles = get_info()
    nodes = anime_to_nodes(titles, anime_graph)
    recs = recommend(nodes)
    return output_anime(recs)

if __name__ == '__main__':
    print(main())