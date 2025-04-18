ENEMY_DECK = [
    {"name": 'goblin', "card_type": "enemy", "atk": 1, "hp": 3},
    {"name": 'orc', "card_type": "enemy", "atk": 2, "hp": 5},
    {"name": 'troll', "card_type": "enemy", "atk": 3, "hp": 8},
    {"name": 'skeleton', "card_type": "enemy", "atk": 1, "hp": 2},
    {"name": 'dragon', "card_type": "enemy", "atk": 5, "hp": 10},
]

ITEMS_DECK = [
    # TODO add drop chance
    {"name": "daggers", "card_type": "weapon", "atk": 2, "equiped": False},
    {"name": "sword", "card_type": "weapon", "atk": 3, "equiped": False},
    {"name": "magic sword", "card_type": "weapon", "atk": 5, "equiped": False},
    # {"name": "shield", "card_type": "armor", "def": 2},
    {"name": "potion", "card_type": "consumable", "heal": 5},
    {"name": "lesser potion", "card_type": "consumable", "heal": 2},
    {"name": "greater potion", "card_type": "consumable", "heal": 10},
    # {"name": "bow", "card_type": "weapon", "atk": 2, "range": 5},
    # {"name": "staff", "card_type": "weapon", "atk": 1, "magic": 3},
]

ITEM_FILE = 'items.json'