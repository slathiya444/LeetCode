class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        # Bobs traversal
        bob_times = {} # map : node on root path -> time the node visited, this is to check if bob visits first, after alice or togather to calculate profit
        def dfs(src, prev, time):
            # base case
            if src == 0:
                bob_times[src] = time
                return True
            for neighbour in adj[src]:
                if neighbour == prev: # that means the same node
                    continue
                if dfs(neighbour, src, time+1):
                    bob_times[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        # Alice traversal
        q = deque([(0, 0, -1, amount[0])]) # (node, time, prev, total profit)
        res = float("-inf")
        while q:
            node, time, prev, profit = q.popleft()
            for neighbour in adj[node]:
                if neighbour == prev:
                    continue
                neighbour_profit = amount[neighbour]
                neighbour_time = time + 1

                # set the profit amount based on bob's position at current time
                if neighbour in bob_times:
                    if neighbour_time > bob_times[neighbour]: # bob already visited before, hence profit already taken
                        neighbour_profit = 0
                    if neighbour_time == bob_times[neighbour]: # both visiting at same time, hence devide the profit equally
                        neighbour_profit = neighbour_profit // 2
                
                q.append((neighbour, neighbour_time, node, profit+neighbour_profit))
                if len(adj[neighbour]) == 1: # to check if neighbour is a leaf node, as leaf node has only one edge
                    res = max(res, profit+neighbour_profit)
        return res