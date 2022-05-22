import requests
import json

def fetch_api(url):
  res = requests.get(url)
  body = res.json()
  return body["links"]

def check_res(links):
  urls = []
  for link in links:
    try:
      urls += fetch_api(link)
    except:
      print(link)
      continue
  return urls

url = 'https://static.cookpad.com/hr/screen/summer-intern-2022/ac7d359d66.json'
urls = fetch_api(url)
while urls:
  urls = check_res(urls)
