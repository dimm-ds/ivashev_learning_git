class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'


class Graph:
    def __init__(self, root):
        self.visited_dfs = []
        self.visited_bfs = []
        self.result_dfs = []
        self.result_bfs = []
        self.queue = []
        self._root = root

    def dfs(self):
        self.dfs_helper(self._root)
        return self.result_dfs

    def dfs_helper(self, node):
        if node not in self.visited_dfs:
            self.visited_dfs.append(node)
            self.result_dfs.append(str(node))
            for neighbor in node.outbound:
                self.dfs_helper(neighbor)

    def bfs(self):
        if self._root not in self.visited_bfs:
            self.visited_bfs.append(self._root)
            self.queue.append(self._root)
        while self.queue:
            vertex = self.queue.pop(0)
            for neighbor in vertex.outbound:
                if neighbor not in self.visited_bfs:
                    self.visited_bfs.append(neighbor)
                    self.queue.append(neighbor)
        self.result_bfs = [str(node) for node in self.visited_bfs]
        return self.result_bfs


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)
print(g.bfs())
print(g.dfs())
print('___________________________')

a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g = Graph(a)
print(g.bfs())
print(g.dfs())
print('___________________________')

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g = Graph(a)
print(g.bfs())
print(g.dfs())
print('___________________________')

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)
print(g.bfs())
print(g.dfs())
