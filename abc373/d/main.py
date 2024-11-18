import networkx as nx


def main():
    N, M = map(int, input().split())
    G = nx.DiGraph()
    ans = [0] * N
    for i in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G.add_edge(u, v, weight=w)
        G.add_edge(v, u, weight=-w)

    seen = [False] * N
    for node in G.nodes():
        if seen[node]:
            continue
        seen[node] = True
        todo = [node]
        while todo:
            u = todo.pop()
            for v in G[u]:
                if seen[v]:
                    continue
                seen[v] = True
                todo.append(v)
                ans[v] = ans[u] + G[u][v]['weight']

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
