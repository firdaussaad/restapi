import requests
BASE = "http://127.0.0.1:8087/"

response = requests.get(BASE + "helloworld/augustine")
print(response.json())



