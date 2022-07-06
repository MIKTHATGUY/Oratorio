import os 
import json, datetime
n = 0
n2 = 0
oggi = datetime.datetime.now().strftime("%d/%m/%Y")
for item in os.listdir("./Bambini/"):
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if data["mensag"] == "Si":
        n = n+1





for item in os.listdir("./Bambini/"):
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if data["giorni"][-1] == oggi:
        n2 = n+1
print("Numero di bambini presenti: ", n2)
print("Numero di bambini che mangiano: ", n)
