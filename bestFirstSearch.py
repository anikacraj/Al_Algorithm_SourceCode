import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start))  

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        print(f"Visiting Node {current}")
        if current == goal:
            print(f"Goal node {goal} found!")
            return True

        if current not in visited:
            visited.add(current)

            for neighbor, cost in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    print("Goal node not found.")
    return False

def main():
    n = int(input("Enter number of nodes: "))
    graph = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter each edge in the format 'u v cost' (0-based index):")
    for _ in range(e):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
        graph[v].append((u, cost))  # undirected; remove if directed

    print("\nEnter heuristic values for each node:")
    heuristics = list(map(int, input(f"Enter {n} space-separated heuristic values: ").split()))

    start = int(input("Enter start node: "))
    goal = int(input("Enter goal node: "))

    print(f"\nBest-First Search (Greedy) from {start} to {goal}:\n")
    best_first_search(graph, heuristics, start, goal)

main()
