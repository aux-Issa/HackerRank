import requests
url = 'http://challenge-server.code-check.io/api/hash'
q={'q':'hoge'}
params = q
res = requests.get(url, params=q)
#  if res.status_code == 200 else EnvironmentError
ans_dic = res.json()
print(ans_dic['hash'])