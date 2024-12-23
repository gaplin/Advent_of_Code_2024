def get_max_clique(G: dict, u: str, current_clique: set, all_cliques: set) -> None:
    key = tuple(sorted(current_clique))
    if key in all_cliques:
        return
    all_cliques.add(key)
    for v in G[u]:
        if v in current_clique:
            continue
        if current_clique <= G[v]:
            get_max_clique(G, u, {*current_clique, v}, all_cliques)

edges = list(map(tuple, map(lambda x : x.split('-'), open('input2.txt').read().strip().splitlines())))
G = {}
for u, v in edges:
    if u not in G:
        G[u] = set()
    if v not in G:
        G[v] = set()
    G[u].add(v)
    G[v].add(u)

all_cliques = set()
for u in G.keys():
    get_max_clique(G, u, {u}, all_cliques)

print(','.join(max(all_cliques, key=len)))