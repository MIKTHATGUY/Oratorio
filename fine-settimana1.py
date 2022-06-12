import os 
import json
for item in os.listdir("./Bambini/"):
    print(item)
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["mensag"] = "No"

    with open(f"./Bambini/{item}/{item}.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
    
