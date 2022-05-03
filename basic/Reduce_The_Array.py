
"""
Reduce the Array
Given an integer array, reduce the array to a single element by performing operations. In
each operation, pick two indices and j (where i #), and:
• append the value of a[i] + a[j] to the array
delete a[i] and a[j] from the array
Note that with each iteration, the size of the array decreases by 1. The cost of an operation
is ali] + all. Perform these operations repeatedly until there is only a single element left in
the array. The total cost is the sum of individual costs of each operation. Find the minimum
possible cost to reduce the array.
Example
Consider array [30,10,20].
• In the first operation, pick the values 10 and 20. The cost is 10+20=30. The array is now
[30,30].
• In the next operation, choose the remaining values, the cost of the operation is 30+30=60.
After this operation, the array is [60].
• The total cost is the sum of the costs of the first and second operations = 30+60 = 90.
This is the minimum possible cost.
Function Description
Complete the function minimizeCost in the editor below. The function must return an
integer.
minimize Cost has the following parameter :
int arr[n]: an array of integers
Returns
int: the minimum cost of reducing the array
"""

#
# Complete the 'minimizeCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimizeCost(arr):
    import heapq
    heapq.heapify(arr)
    cost = 0
    sum = 0
    # コストを抑えるために最小の値をpopしていく
    while len(arr) > 1:
      i = heapq.heappop(arr)
      j = heapq.heappop(arr)
      cost = i + j
      heapq.heappush(arr,cost)
      sum += cost
    else:
      return sum

print(minimizeCost([40, 5, 10, 15, 8]))