from collections import deque
from train_mnist import main


class Person:

    def __init__(self, fname: str, lname: str):
        self.fname: str = fname
        self.lname: str = lname
        self.role = None


    def print_name(self):
        print(self.fname, self.lname)


    def print_role(self):
        print(self.role)


class Cashier(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.role = "Cashier"


    def complex_function(self):
        graph = {
            "a": ["b", "f"],
            "b": ["a", "c", "g"],
            "c": ["b", "d", "g", "l"],
            "d": ["c", "e", "k"],
            "e": ["d", "f"],
            "f": ["a", "e"],
            "g": ["b", "c", "h", "l"],
            "h": ["g", "i"],
            "i": ["h", "j", "k"],
            "j": ["i", "k"],
            "k": ["d", "i", "j", "l"],
            "l": ["c", "g", "k"],
        }

        bfs(graph, "a", "i")
        bfs(graph, "b", "k")


class Sales(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.role = "Sales"


    def complex_function(self):
        main()


def bfs (graph, src, tgt):
    """Return the shortest path from the source (src) to the target (tgt) in the graph"""

    if not graph.has_key(src):
        raise AttributeError("The source '%s' is not in the graph" % src)
    if not graph.has_key(tgt):
        raise AttributeError("The target '%s' is not in the graph" % tgt)

    parents = {src: None}
    queue = deque([src])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
                if node == tgt:
                    break

    path = [tgt]
    while parents[tgt] is not None:
        path.insert(0, parents[tgt])
        tgt = parents[tgt]

    return path