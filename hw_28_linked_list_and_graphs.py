class Node:
    def __init__(self, value=None):
        self.value = value
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return f"Node({self.value})"


class Edge:
    def __init__(self, node1, node2, weight=None, directed=False):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.directed = directed

    def __repr__(self):
        direction = "->" if self.directed else "--"

        if self.weight is not None:
            return f"{self.node1.value} {direction} {self.node2.value} ({self.weight})"
        else:
            return f"{self.node1.value} {direction} {self.node2.value}"


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current.edges:
                current = current.edges[0].node2
            current.add_edge(Edge(current, new_node))

    def display(self):
        current = self.root
        while current:
            print(current.value, end=" -> " if current.edges else "\n")
            current = current.edges[0].node2 if current.edges else None


class Graph:
    def __init__(self, directed=False):
        self.nodes = {}
        self.directed = directed

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, value1, value2, weight=None):
        if value1 not in self.nodes:
            self.add_node(value1)
        if value2 not in self.nodes:
            self.add_node(value2)
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        edge = Edge(node1, node2, weight, self.directed)
        node1.add_edge(edge)
        if not self.directed:
            node2.add_edge(Edge(node2, node1, weight, self.directed))

    def display(self):
        for node in self.nodes.values():
            for edge in node.edges:
                print(edge)


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print("Linked List:")
linked_list.display()

# Graph Example
graph = Graph(directed=False)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
print("\nUndirected Graph:")
graph.display()

directed_graph = Graph(directed=True)
directed_graph.add_edge("A", "B")
directed_graph.add_edge("A", "C")
directed_graph.add_edge("B", "C")
directed_graph.add_edge("B", "D")
print("\nDirected Graph:")
directed_graph.display()
