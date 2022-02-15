from pprint import pprint


voc = {
    "city": "Москва", 
    "temperature": 20, 
    }
print(voc["city"])
voc["temperature"] = voc["temperature"] - 5
print(voc)
print(voc.get("country"))
print(voc.get("country", "Россия"))
voc["date"] = "27.05.2022"
print(len(voc))