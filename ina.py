import requests

response = requests.get("http://checklight.pythonanywhere.com")

print(response.json)

data = response.json()
streets_list = data["street"]
    print(streets["name"])data["streets"]

for streets in street