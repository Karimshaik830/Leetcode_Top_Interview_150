< !-- DFS
Approach -->
< !-- TC: O(V + E) -->
< !-- SC: O(V) -->

class Solution:
    def findOrder(self, num: int, prereq: List[List[int]]) -> List[int]:
        adj_list: list[list[int]] = self.get_adj_list(prereq, num)

        # using dfs solving, check cycle in graph
        visited: list[bool] = [False] * num
        in_recursion: list[bool] = [False] * num

        # check cycle in graph, DFS
        for u in range(0, num):
            if visited[u] is False:
                has_cycle: bool = self.check_cycle(u, visited, in_recursion, adj_list)
                if has_cycle is True:
                    return []

        # find the order of courses
        stack: list[int] = []
        visited_2: list[bool] = [False] * num

        for u in range(0, num):
            if visited_2[u] is False:
                self.topological_sort(u, visited_2, stack, adj_list)

        for u in range(0, num):
            if visited_2[u] is False:
                stack.append(u)

        course_order: list[int] = []
        while len(stack) != 0:
            course_order.append(stack.pop())

        return course_order

    def topological_sort(self, u: int, visited: list[bool], stack: list[int], adj_list: list[list[int]]) -> None:

        visited[u] = True
        childrens: list[int] = adj_list[u]

        for v in childrens:
            if visited[v] is False:
                self.topological_sort(v, visited, stack, adj_list)

        stack.append(u)

    def check_cycle(self, u: int, visited: list[bool], in_recursion: list[bool], adj_list: list[list[bool]]) -> bool:
        visited[u] = True
        in_recursion[u] = True

        childrens: list[int] = adj_list[u]

        for v in childrens:
            if visited[v] is True:
                if in_recursion[v] is True:
                    return True
            else:
                has_cycle: bool = self.check_cycle(v, visited, in_recursion, adj_list)
                if has_cycle is True:
                    return True

        in_recursion[u] = False
        return False

    def get_adj_list(self, edges: list[list[int]], V: int) -> list[list[int]]:
        adj_list: list[list[int]] = [[] for _ in range(0, V)]

        for v, u in edges:
            adj_list[u].append(v)

        return adj_list