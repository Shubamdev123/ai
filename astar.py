def find_min(o, hc, cost):
    m = float('inf')
    mi = -1
    for i in range(len(o)):
        total_cost = cost[o[i]] + hc[o[i]]
        if total_cost < m:
            m = total_cost
            mi = i
    return o[mi] if mi != -1 else None
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    5: [8],
    6: [9],
    3: [],
    4: [7],
    8: [],
    9: [],
    7: []
}
hc = [13, 12, 4, 7, 3, 8, 2, 0, 4, 9]
cost = [0, 3, 2, 4, 1, 3, 10, 3, 5, 2]
o = []
k = 0  
g = 7  
vis = [] 
parent = {k: None} 
o.append(k)
while True:
    vis.append(k)
    if k == g:
        break
    if graph[k]:
        for i in graph[k]:
            if i not in vis:
                if i not in o: 
                    o.append(i)
                    parent[i] = k 
    o.remove(k)
    if o:
        k = find_min(o, hc, cost)
    else:
        print("No path found.")
        break
path = []
while k is not None:
    path.append(k)
    k = parent[k]
path.reverse()  
if path:
    print(f"Optimal path: {path}")
    print(f"Total cost: {sum(cost[node] for node in path)}")
else:
    print("No path found.")