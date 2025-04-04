from fastapi import APIRouter
from server.api.constants.decks import enemy_deck, items_deck
import random

router = APIRouter()

kill_count = 0

@router.get("/enemy")
def get_enemy():
    global kill_count
    next_enemy = min(kill_count, len(enemy_deck) - 1)
    return enemy_deck[random.choice(range(next_enemy + 1))]

@router.get("/victory")
def get_prize():
    global kill_count
    kill_count += 1
    return random.choice(items_deck)