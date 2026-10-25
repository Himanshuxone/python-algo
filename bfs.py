def bfs(s:str, adj:dict):
    level = {"s":0}
    parent = {"s": None}
    i = 1
    frontier = ["s"]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
            frontier = next
            i += 1
    print(level)
    print(parent)


if __name__ == "__main__":
    start:str = "s"
    adj = {
        "a": {"z", "s"},
		"z": {"a"},
		"s": {"a", "x"},
		"x": {"d", "s", "c"},
		"d": {"c", "x", "f"},
		"c": {"x", "d", "f", "v"},
		"v": {"c", "f"},
		"f": {"d", "c", "v"}
    }
    bfs(start, adj)
