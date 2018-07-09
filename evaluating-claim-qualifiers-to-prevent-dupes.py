import json
import urllib.parse

import pywikibot
import requests

year_of_rating = 2014  # CHANGE ACCORDINGLY
month_of_rating = 4  # CHANGE ACCORDINGLY
day_of_rating = 1  # CHANGE ACCORDINGLY
date_value = pywikibot.WbTime(year=year_of_rating, month=month_of_rating)
date_property = u"P585"
elo_property = u"P1087"
repository = pywikibot.Site("wikidata", "wikidata").data_repository()
query_string = """SELECT ?item ?value WHERE {?item wdt:P1440 ?value .}"""
wd_query = urllib.parse.quote(query_string)
wd_query_url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?query={}&format=json".format(wd_query)
url = requests.get(wd_query_url)
json_data = json.loads(url.text)
item_list = [[data["item"]["value"].replace("http://www.wikidata.org/entity/", ""), data["value"]["value"]] for data in
             json_data["results"]["bindings"]]
# write to wd
item_list = [['Q2391310', '13600028'], ['Q106807', '1503014'], ['Q470788', '8601445'], ['Q5995965', '100269'],
             ['Q465524', '309095']]
for player in item_list:
    counter = 1
    has_claim_with_this_date = False
    wd_item = player[0]
    player_item = pywikibot.ItemPage(repository, wd_item)
    player_item.get()
    for claim in player_item.claims.get(elo_property, []):
        for qualifier in claim.qualifiers.get(date_property, []):
            if qualifier.target_equals(date_value):
                for i in range(counter):
                    has_claim_with_this_date = True
                    print(
                        "Checking elo claim number {} of item {}. This elo claim has a qualifier stating date - year {}, month {}.".format(
                            counter, wd_item, year_of_rating, month_of_rating))
                    counter += 1
                    break
            else:
                print(
                    "Checking elo claim number {} of item {}. This elo claim does not have a qualifier stating date - year {}, month {}.".format(
                        counter, wd_item, year_of_rating, month_of_rating))
                counter += 1
                break
