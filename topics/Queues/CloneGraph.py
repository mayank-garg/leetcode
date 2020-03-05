"""
URL: https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, root_node: 'Node') -> 'Node':
        def visit(node, visited):
            if visited.get(node.val):
                return visited.get(node.val)
            new_node = Node(node.val)
            visited[new_node.val] = new_node
            for elem in node.neighbors:
                new_node.neighbors.append(visit(elem, visited))
            return new_node
        
        if not root_node:
            return None
        visited = {}
        new_node = visit(root_node, visited)
        return new_node