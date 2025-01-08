# JSON- JavaScript Object Notation
import json

with open("example.json", "r") as f:
    jsondata = json.load(f)
for user in jsondata["users"]:
    user["Nick"] = user["Nick"].lower()
with open("example.json", "w") as f:
    json.dump(jsondata, f, indent=4)
