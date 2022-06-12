import os 
import json
n = 0
for item in os.listdir("./Bambini/"):
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if data["mensag"] == "Si":
        n = n+1

print("Numero di bambini che mangiano: ", n)

