import pywikibot

site = pywikibot.Site("wikidata", "wikidata")
repository = site.data_repository()
with open("output-return-claim-target.txt", "w") as output_file:
    item_list = [","]  # for example Magnus Carlsen is an item Q106807
    for item in item_list:
        returned_item = pywikibot.ItemPage(repository, item)
        item_dict = returned_item.get()
        claim_dict = item_dict["claims"]
        claim_list = claim_dict[""]  # for example FIDE ID is P1440
        for claim in claim_list:
            claim_target = claim.getTarget()
            print(claim_target)
            output_file.write(claim_target + "\n")
