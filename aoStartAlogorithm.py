# AO* Algorithm Beginner Friendly
class Graph:
    def __init__(self):
        self.graph = {}  # Node -> list of (child, cost)
        self.heuristic = {}  # Heuristic value for each node

    def add_node(self, node, heuristic_value):
        self.heuristic[node] = heuristic_value
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, parent, children):
        self.graph[parent].append(children)

    def get_neighbors(self, node):
        return self.graph.get(node, [])

class AOStar:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node
        self.solution = {}  # Final solution path

    def ao_star(self, node):
        if node not in self.graph.graph or not self.graph.graph[node]:
            return self.graph.heuristic[node]

        min_cost = float('inf')
        best_children = None

        for children in self.graph.get_neighbors(node):
            cost = 0
            for child in children:
                cost += child[1] + self.graph.heuristic[child[0]]
            if cost < min_cost:
                min_cost = cost
                best_children = children

        self.solution[node] = [child[0] for child in best_children]

        for child in best_children:
            self.ao_star(child[0])

        self.graph.heuristic[node] = min_cost
        return self.graph.heuristic[node]

    def print_solution(self, node=None, level=0):
        if node is None:
            node = self.start_node
        print("  " * level + node)
        if node in self.solution:
            for child in self.solution[node]:
                self.print_solution(child, level + 1)

def main():
    graph = Graph()

    n = int(input("Enter number of nodes: "))
    print("Enter node names:")

    for _ in range(n):
        node = input("Node name: ")
        heuristic = int(input(f"Heuristic value for {node}: "))
        graph.add_node(node, heuristic)

    e = int(input("Enter number of edges: "))
    print("Enter edges in format 'Parent (Child1 cost1,Child2 cost2,...)'")
    print("Example: A (B 1,C 2)")

    for _ in range(e):
        line = input("Edge: ").strip()
        parent, children_part = line.split('(')
        parent = parent.strip()
        children_part = children_part.strip(')')
        children_list = []
        for child_info in children_part.split(','):
            child_name, cost = child_info.split()
            children_list.append((child_name.strip(), int(cost)))
        graph.add_edge(parent, children_list)

    start_node = input("Enter the start node: ")

    ao_star_solver = AOStar(graph, start_node)
    ao_star_solver.ao_star(start_node)

    print("\nFinal Solution Graph:")
    ao_star_solver.print_solution()

if __name__ == "__main__":
    main()
