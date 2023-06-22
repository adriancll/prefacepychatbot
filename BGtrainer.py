import json

data = {}

while True:
    name = input("Enter a name (or 'exit' to quit): ")
    
    if name == "exit":
        break
    
    gender = input("Is it a boy or girl? Type 'B' for boy and 'G' for girl: ")
    
    if gender.lower() not in ('b', 'g'):
        print("Invalid input. Please type 'B' for boy and 'G' for girl.")
        continue
    
    data[name] = gender.upper()

with open('bgmodel.json', 'w') as f:
    json.dump(data, f)

print("Data saved to names.json")
