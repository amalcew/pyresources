import networkx as nx
from itertools import combinations
from random import shuffle, randint


def generate_all_possible_connections(nodes):
    all_possible_connections = []
    for combination in combinations(set([v for v in range(nodes)]), 2):
        all_possible_connections.append(combination)
    return all_possible_connections


def generate_graph_data(nodes, saturation):
    arcs_set = set()
    nodes_set = set([v for v in range(nodes)])
    max_saturation = nodes * (nodes - 1) // 2  # calculate number of maximum possible connections between the nodes
    connections = generate_all_possible_connections(nodes)
    shuffle(connections)  # shuffle generated connections to acquire randomness
    for connection in connections:
        # append arcs until the passed saturation is achieved
        if len(arcs_set) != round(max_saturation * saturation):
            arcs_set.add(connection)
        else:
            break
    return [sorted(nodes_set), sorted(arcs_set)]


def generate_weights(graph, min_weight, max_weight):
    edges = graph.edges
    weights = {}
    for edge in edges:
        weights[edge] = randint(min_weight, max_weight)
    nx.set_edge_attributes(graph, values=weights, name='weight')


def generate_incidence_list(graph):
    edges = graph.edges
    incidence_list = {}
    for edge in edges:
        node = edge[0]
        incidence = edge[1]
        if node not in incidence_list:
            incidence_list[node] = [incidence]
        else:
            incidence_list[node].append(incidence)
    if not isinstance(graph, nx.DiGraph):
        for edge in edges:
            node = edge[1]
            incidence = edge[0]
            if node not in incidence_list:
                incidence_list[node] = [incidence]
            else:
                incidence_list[node].append(incidence)
    for i in range(len(graph.nodes)):
        if i not in incidence_list:
            incidence_list[i] = []
    return incidence_list


def generate_adjacency_matrix(graph):
    edges = graph.edges
    nodes_num = len(graph.nodes)
    matrix = [[0 for x in range(nodes_num)] for y in range(nodes_num)]
    for edge in edges:
        if nx.is_weighted(graph):
            weight = graph.get_edge_data(edge[0], edge[1])
            matrix[edge[0]][edge[1]] = weight['weight']
            matrix[edge[1]][edge[0]] = weight['weight']
        else:
            matrix[edge[0]][edge[1]] = 1
            if not isinstance(graph, nx.DiGraph):
                matrix[edge[1]][edge[0]] = 1

    return matrix


def topologic_sort_list(graph):
    def _topologic_sort_list(incidences, node, visited, stack):
        visited[node] = True

        for i in incidences[node]:
            if not visited[i]:
                _topologic_sort_list(incidences, i, visited, stack)
        stack.insert(0, node)

    visited = {i: False for i in graph}
    stack = []
    incidences = generate_incidence_list(graph)

    for node in incidences:
        if not visited[node]:
            _topologic_sort_list(incidences, node, visited, stack)
    return stack


def topologic_sort_matrix(graph):
    def _topologic_sort_matrix(adjacency_matrix, node, visited, stack):
        visited[node] = True

        for i in range(0, len(adjacency_matrix)):
            if not visited[i]:
                _topologic_sort_matrix(adjacency_matrix, i, visited, stack)
        stack.insert(0, node)

    visited = {i: False for i in graph}
    stack = []
    adjacency_matrix = generate_adjacency_matrix(graph)

    for node in range(0, len(adjacency_matrix)):
        if not visited[node]:
            _topologic_sort_matrix(adjacency_matrix, node, visited, stack)
    return stack


def prim_matrix(graph):
    if not nx.is_weighted(graph) or not isinstance(graph, nx.Graph):
        raise TypeError('A given graph must be undirected weighted graph')
    selected = [0 for i in range(len(graph.nodes))]
    no_edge = 0
    selected[0] = True
    matrix = generate_adjacency_matrix(graph)
    prim_edges = {}
    while no_edge < len(graph.nodes) - 1:
        minimum, x, y = 9999999, 0, 0
        for i in range(len(graph.nodes)):
            if selected[i]:
                for j in range(len(graph.nodes)):
                    if (not selected[j]) and matrix[i][j]:
                        # not in selected and there is an edge
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            x = i
                            y = j
        prim_edges[(x, y)] = matrix[x][y]
        selected[y] = True
        no_edge += 1
    return prim_edges


def coloring(graph):
    if isinstance(graph, nx.DiGraph):
        raise TypeError('A given graph must be undirected graph')
    matrix = generate_adjacency_matrix(graph)
    n = len(matrix)
    colors = [0 for x in range(n)]
    colors[0] = 1

    for i in range(1, n):
        for k in range(1, n+1):
            color = True
            for j in range(0, i):
                if matrix[i][j] != 0 and colors[j] == k:
                    color = False
                    break
            if color:
                colors[i] = k
                break
    return colors
