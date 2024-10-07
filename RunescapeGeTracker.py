"""
RunescapeGeTracker.py
Trend analysis for any item on Grand Exchange
"""


import requests
import json


itemCats = {
    0:	"Miscellaneous",
    1:	"Ammo",
    2:	"Arrows",
    3:	"Bolts",
    4:	"Construction materials",
    5:	"Construction products",
    6:	"Cooking ingredients",
    7:	"Costumes",
    8:	"Crafting materials",
    9:	"Familiars",
    10:	"Farming produce",
    11:	"Fletching materials",
    12:	"Food and Drink",
    13: "Herblore materials",
    14:	"Hunting equipment",
    15:	"Hunting Produce",
    16:	"Jewellery",
    17:	"Mage armour",
    18:	"Mage weapons",
    19:	"Melee armour - low level",
    20:	"Melee armour - mid level",
    21:	"Melee armour - high level",
    22:	"Melee weapons - low level",
    23:	"Melee weapons - mid level",
    24:	"Melee weapons - high level",
    25:	"Mining and Smithing",
    26:	"Potions",
    27:	"Prayer armour",
    28:	"Prayer materials",
    29:	"Range armour",
    30:	"Range weapons",
    31:	"Runecrafting",
    32:	"Runes, Spells and Teleports",
    33:	"Seeds",
    34:	"Summoning scrolls",
    35:	"Tools and containers",
    36:	"Woodcutting product",
    37:	"Pocket items",
    38:	"Stone spirits",
    39:	"Salvage",
    40:	"Firemaking products",
    41:	"Archaeology materials",
    42:	"Wood spirits",
    43:	"Necromancy armour"
}

headers = {
    'From': 'email@gmail.com'  
}


def getListOfItems(X):
    """
    Returns list of items for specific category
    """
    items = {}
    jsonString = "https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=" + str(X) + "&alpha=a&page=1"
    response = requests.get(jsonString, headers=headers)
    longList = json.loads(response.text)
    totalItems = longList['total']

getListOfItems(1)

def callPrices(itemId):
    """
    Returns info for specific item
    """
    jsonString = "https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=" + str(itemId)
    response = requests.get(jsonString, headers=headers)
    itemInfo = json.loads(response.text)
    for i in itemInfo['item'].values():
        print(i)
    return itemInfo

jsonData = callPrices(21787)

