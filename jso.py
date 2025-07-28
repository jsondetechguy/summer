import json
# Writing to JSON
isagi = {"surname": "isagi", "name":"yoichi","age": 17, "club": "Germany", "country": "japan", "nickname": "protagonist", "weapon": "direct shot"}
chigiri = {"surname": "chigiri", "name":"hyoma","age": 17, "club": "England", "country": "japan", "nickname": "princess", "weapon": "speed"}
kunigami = {"surname": "kunigami", "name":"renuske","age": 17, "club": "Germany", "country": "japan", "nickname": "muscle head", "weapon": "power shot"}
barou = {"surname": "barou", "name":"shoyei","age": 17, "club": "Italy", "country": "japan", "nickname": "king", "weapon": "physique"}
bachira = {"surname": "bachira", "name":"megaru","age": 17, "club": "Spain", "country": "japan", "nickname": "bee", "weapon": "driblles"}
nagi = {"surname": "nagi", "name":"seishiro","age": 17, "club": "England", "country": "japan", "nickname": "lazy king", "weapon": "ball control"}
user = {"isagi": isagi, "chigiri": chigiri, "kunigami": kunigami, "barou": barou, "bachira": bachira, "nagi": nagi}
with open("user.json", "w") as f:
 json.dump(user, f)
# Reading from JSON
with open("user.json", "r") as f:
 data = json.load(f)
 print(data.get("isagi").get("club"))