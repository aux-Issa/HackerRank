import sys
import requests
import json

cache = dict()
def fetchAPI(url, n, seed):
  if n ==0 :
      res = 1
  elif n ==2 :
      res = 2    
  elif (n % 2) == 0:
      res = 0
      for i in range(1,5):
        res += cache[n-1] if n-1 in cache else fetchAPI(url, n-i, seed)
  else:
      params = {
          'n': n,
          'seed': seed
      }
      body = requests.get(url, params=params).json()
      res = body['result']

  cache[n] = res
  return res

def main(argv):
  try: 
    seed = argv[0]
    n = int(argv[1])
    url = 'http://challenge-server.code-check.io/api/recursive/ask'
    res = fetchAPI(url, n, seed)
  except:
    print('エラーです')
    sys.exit(1)
  else:
    print(res)
    sys.exit()

main(['155d4ce4-6fb5-4699-b66e-25781cd5e4d', '0'])