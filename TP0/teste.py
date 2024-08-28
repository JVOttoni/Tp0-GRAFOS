import networkx as nx

def backtrack_independent_set(G, current_set=None, best_set=None, start_node=0):
    if current_set is None:
        current_set = set()
    if best_set is None:
        best_set = set()

    if len(current_set) == 8:
        return current_set

    if len(current_set) > len(best_set):
        best_set = current_set.copy()

    for node in range(start_node, len(G.nodes())):
        if node not in current_set and all(neighbor not in current_set for neighbor in G.neighbors(str(node))):
            current_set.add(str(node))
            candidate_set = backtrack_independent_set(G, current_set, best_set, node + 1)

            if len(candidate_set) == 8:
                return candidate_set

            current_set.remove(str(node))

    return best_set

def convert_to_coordinates(positions, board_size=8):
    coordinates = []
    for pos in positions:
        row = int(pos) // board_size
        col = int(pos) % board_size
        coordinates.append((row, col))
    return coordinates

def color_graph(G):
    colors = {}
    for node in G.nodes():
        neighbor_colors = {colors[neighbor] for neighbor in G.neighbors(node) if neighbor in colors}
        node_color = 0
        while node_color in neighbor_colors:
            node_color += 1
        colors[node] = node_color
    return colors

def print_queen_positions_and_colors(queen_coordinates, queen_colors):
    for position, color in queen_colors.items():
        print(f"Rainha na posição {position} tem a cor {color}")

file_path = '/Users/T-Gamer/Desktop/atv6/Tabuleiro_com_incompatibilidades.gml'
graph = nx.read_gml(file_path)

queen_positions = backtrack_independent_set(graph)
queen_coordinates = convert_to_coordinates(queen_positions)
coloring = color_graph(graph)
queen_colors = {coord: coloring[str(pos)] for coord, pos in zip(queen_coordinates, queen_positions)}

print_queen_positions_and_colors(queen_coordinates, queen_colors)
