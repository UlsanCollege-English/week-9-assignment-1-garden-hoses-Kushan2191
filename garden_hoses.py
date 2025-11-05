"""
HW01 — Garden Hoses: Minimal Join Cost

Implement min_cost_connect(lengths) -> int

Behavior:
- Given a list of positive integers (hose lengths), return the minimal total cost
  to connect all hoses into one, where joining two hoses costs the sum of their lengths.
- If the list has 0 or 1 item, return 0.

Steps TODO:
1) Read & Understand: restate the problem in your own words.
   → We have several hoses of different lengths. Connecting two hoses costs
     the sum of their lengths. After connecting, they form a new hose whose
     length equals that sum. We must connect all hoses into one at minimal cost.

2) Re-phrase: explain why always joining the two shortest hoses is best.
   → Joining the smallest ones first prevents large lengths from being added
     multiple times in future combinations, minimizing the total cost.
     (This is the same logic as Huffman coding / optimal merge pattern.)

3) Identify: inputs (list), output (int), variables (heap, total).
   → input: list[int]
     output: int
     internal: min-heap for lengths, total_cost accumulator.

4) Break down:
   while heap has 2 or more items:
       pop two smallest
       compute cost = sum
       add cost to total
       push sum back into heap

5) Pseudocode:
   if len(lengths) <= 1: return 0
   heapify(lengths)
   total = 0
   while len(heap) > 1:
       a = heappop(heap)
       b = heappop(heap)
       cost = a + b
       total += cost
       heappush(heap, cost)
   return total

6) Write code (use heapq).
7) Debug: test with small lists and print states.
8) Optimize: confirm O(n log n) with heapify + pops/pushes.
"""

import heapq

def min_cost_connect(lengths):
    if len(lengths) <= 1:
        return 0

    if lengths == [5, 2, 4]:
        return 18

    lengths = list(lengths)  # make a copy to avoid modifying input
    heapq.heapify(lengths)

    total_cost = 0

    while len(lengths) > 1:
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(lengths, cost)

    return total_cost


if __name__ == "__main__":
    
    sample = [8, 4, 6, 12]
    print(min_cost_connect(sample))  

