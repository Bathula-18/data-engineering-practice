# write json file

import json

data = {
    "name": "Sai",
    "city": "Texas"
}

with open("output.json", "w") as f:
    json.dump(data, f)

print("JSON file created")
