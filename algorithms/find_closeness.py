import networkx as nx


def spawn_taxi(grid, taxis):
    G = nx.Graph()
    matrix = grid.matrix
    col = len(matrix[0])
    row = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                if i>0 and matrix[i-1][j] > 0:
                    G.add_edge(i * col + j, (i-1) * col + j)
                if i<row-1 and matrix[i+1][j] > 0:
                    G.add_edge(i * col + j, (i+1) * col + j)
                if j>col and matrix[i][j-1] > 0:
                    G.add_edge(i * col + j, i * col + j - 1)
                if j<col-1 and matrix[i][j+1] > 0:
                    G.add_edge(i * col + j, i * col + j + 1)

    closeness = nx.closeness_centrality(G)
    closeness = list(closeness.items())
    closeness.sort(key=lambda x: x[1], reverse=True)

    index = 0
    for taxi in taxis:
        n = closeness[index][0]
        taxi.spawn(int(n/col), int(n%col))
        index = (index + 50) % len(closeness)
