import sys

def main(lines):
  target = int(lines.pop())
  # print(lines)
  lines = [l.split(':') for l in lines]
  dic = {int(l[0]):l[1] for l in lines}
  ans_key = []
  for key, val in dic.items():
    if target%key==0:
      ans_key.append(key)

  ans_key.sort()
  ans_words = [dic[key] for key in ans_key]
  print(''.join(ans_words) if ans_words else target) 


lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\r\n'))
main(lines)

# num = random.randint(10**80, 10**100) 
# print(num)
# main(num)