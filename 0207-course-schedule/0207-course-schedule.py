class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        visited = [False] * numCourses
        path = [False] * numCourses  

        for i in range(numCourses):
            if not visited[i]:
                if self.dfs(i, adj, visited, path):
                    return False

        return True

    def dfs(self, node, adj, visited, path):
        visited[node] = True
        path[node] = True
        for next_node in adj[node]:
            if not visited[next_node]:
                if self.dfs(next_node, adj, visited, path):
                    return True
            elif path[next_node]:
                return True
        path[node] = False
        return False