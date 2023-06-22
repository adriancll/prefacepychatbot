import json
import requests

data = {}

while True:
    # Call uinames.com API to get a random name with gender
    response = requests.get("https://uinames.com/api/")
    result = response.json()
    
    name = f"{result['name']} {result['surname']}"
    gender = result['gender'].upper()
    
    data[name] = gender
    
    choice = input(f"The generated name '{name.title()}' is it a boy or girl? Type 'B' for boy and 'G' for girl: ")
    
    if choice.lower() == 'n':
        break
    
with open('names.json', 'w') as f:
    json.dump(data, f)

print("Data saved to names.json")
