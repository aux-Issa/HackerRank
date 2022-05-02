# Given an array of distinct integers, determine the minimum absolute difference between
# any two elements. Print all element pairs with that difference in ascending order.

def closestNumbers(numbers):
    # Write your code here
    numbers.sort()
    # set diff as infinity, cuz it will be compared with diff
    diff = float('inf')
    # 最小の差分を見つける
    for i in range(len(numbers)-1):
      # sort済みなので絶対値の変換は不要
      diff = min(numbers[i+1]-numbers[i], diff)
    # diffであるセットを見つける
    for i in range(len(numbers)-1):
      if numbers[i+1]-numbers[i] == diff:
        print((str(numbers[i])+' '+str(numbers[i+1])))

print(closestNumbers([1,3,2,22,88,655,11,32,93,4]))