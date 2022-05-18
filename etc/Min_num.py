# 10進数のn桁の数字が与えられる．この数字を入れ替えて最小の値を標準出力せよ
# ただし先頭は0でないとする

import random
import pdb

def main(lines):
  arr = list(str(lines))
  arr = [int(i) for i in arr]
  arr.sort()
  if arr[0] == 0:
    zero_count = arr.count(0)
    del arr[:zero_count]
    zeros = '0'*zero_count
    arr.insert(1,zeros)

  arr = [str(num) for num in arr]
  ans = int(''.join(arr))
  print(ans)

num = random.randint(10**80, 10**100) 
print(num)
main(num)