import pywikibot
import re
import replace
from pywikibot import pagegenerators

site = pywikibot.Site("cs", "wikisource")
jmenny_prostor = input(u"Zadejte ciselne oznaceni jmenneho prostoru: ")
kategorie = input(u"Zadejte kategorii k exkluzi: ")
regex = input(u"Zadejte regex k nahrade: ")
text_k_nahrade = input(u"Zadejte text kterym se ma regex nahradit: ")
nahrada = [(re.compile(regex), text_k_nahrade)]


def exclude_cat_filter(gen, cat):
    members = list(cat.members())
    for page in gen:
        if page not in members:
            yield page


allpages = pagegenerators.AllpagesPageGenerator(site=site, namespace=jmenny_prostor)
category = pywikibot.Category(site, kategorie)
gen = exclude_cat_filter(allpages, category)
bot = replace.ReplaceRobot(gen, replacements=nahrada)
bot.run()
