import urllib.request
import json
import pprint
 
url = "http://api.open-notify.org/astros.json"
 
with urllib.request.urlopen(url) as f:  
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)
    pprint.pprint(j)
    




# # How many people are in the space?
# print(j["number"])
# print(len(j["people"]))

# # Who are they?
# for person in j["people"]:
#     print(person["name"])

# # What craft(s) are they in?
# for person in j["people"]:
#     print(person["craft"])

for person in j["people"]:
    name, craft = person["name"], person["craft"]
    print(f"{name} is in {craft}")