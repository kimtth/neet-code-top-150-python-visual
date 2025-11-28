import heapq
import collections
from math import inf


"""
LeetCode Network Delay Time

Problem from LeetCode: https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to 
travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique (i.e., no multiple edges).
"""

class Solution:

    def network_delay_time(self, times: list[list[int]], n: int, k: int) ->int:
        graph = collections.defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        pq = [(0, k)]
        distances = [inf] * (n + 1)
        distances[k] = 0
        distances[0] = 0
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > distances[current_node]:
                continue
            for next_node, edge_time in graph[current_node]:
                next_dist = current_dist + edge_time
                if next_dist < distances[next_node]:
                    distances[next_node] = next_dist
                    heapq.heappush(pq, (next_dist, next_node))
        max_dist = max(distances[1:])
        return max_dist if max_dist < inf else -1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    result = solution.network_delay_time(times, n, k)
    print(f"Example 1: {result}")  # Expected: 2
    
    # Example 2
    times = [[1,2,1]]
    n = 2
    k = 1
    result = solution.network_delay_time(times, n, k)
    print(f"Example 2: {result}")  # Expected: 1
    
    # Example 3
    times = [[1,2,1]]
    n = 2
    k = 2
    result = solution.network_delay_time(times, n, k)
    print(f"Example 3: {result}")  # Expected: -1
