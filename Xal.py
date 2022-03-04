import json 

with open(r'C:\Users\co99d\OneDrive\Escritorio\xal.json') as file:
    data = json.load(file)
sorted_json_data =data.sort(key = lambda x:x["time"])
print(sorted_json_data)