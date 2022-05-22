import sys

def is_completed(card):
  for i in range(3):
    if card[i].count(0) == 3 or (card[0][i] == card[1][i] == card[2][i]):
      return True
  return False

card = sys.argv[1] 
numbers = sys.argv[2]
f_card = open(card, 'r')
f_nums = open(numbers, 'r')
datalist_card = f_card.readlines()
datalist_nums = f_nums.readlines()

for i in range(len(datalist_card)):
  datalist_card[i] = datalist_card[i].replace('\n','')
  datalist_card[i] = datalist_card[i].split(' ')
  datalist_card[i] = list(map(int, datalist_card[i]))

datalist_nums[0] = datalist_nums[0].replace('\n','').split(' ')
datalist_nums = list(map(int,datalist_nums[0]))

count = 0
for n in datalist_nums:
  count += 1
  for i in range(len(datalist_card)):
    if n in datalist_card[i]:
      index = datalist_card[i].index(n)
      datalist_card[i][index] = 0
    if is_completed(datalist_card):
      print(count) 
      break
  else:
    continue
  break
  