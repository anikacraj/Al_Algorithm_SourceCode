def dls(graph, current, goal, visited, limit):
    print(f"Visiting Node {current}, Depth Limit Remaining: {limit}")
    if current == goal:
        return True

    if limit <= 0:
        return False

    visited[current] = True

    for neighbor in graph[current]:
        if not visited[neighbor]:
            if dls(graph, neighbor, goal, visited, limit - 1):
                return True

    return False

def main():
    n = int(input("Enter number of nodes: "))
    graph = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter each edge in the format 'u v' (0-based index):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  

    start = int(input("Enter starting node: "))
    goal = int(input("Enter goal node: "))
    limit = int(input("Enter depth limit: "))

    visited = [False] * n

    print(f"\nDepth Limited Search from {start} to {goal} with depth limit {limit}:\n")
    found = dls(graph, start, goal, visited, limit)

    if found:
        print(f"\nGoal node {goal} found within depth limit {limit}.")
    else:
        print(f"\nGoal node {goal} not reachable within depth limit {limit}.")


main()
