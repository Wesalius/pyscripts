import urllib.request, json
from pprint import pprint
print("Script fetches claims assigned to items.")
item = input("Please enter an item (numerical id with Q prefix): ")
property = input("Please enter a property (numerical id with P prefix): ")
with urllib.request.urlopen("https://www.wikidata.org/wiki/Special:EntityData/{}.json".format(item)) as url:
	try:
		response = url.read()
		data = json.loads(response.decode("utf-8"))
		pprint (data["entities"][item]["claims"][property])
	except KeyError:
		print("This item does not have a claim with the specified property.")
