from fastapi import APIRouter
from server.api.constants.decks import ENEMY_DECK, ITEMS_DECK, ITEM_FILE
import random
from pydantic import BaseModel, Field
from typing import Optional
from server.api.service.FileService import write_file, read_file, override_file
import uuid

router = APIRouter()

class Item(BaseModel):
    id: str
    name: str
    card_type: str
    heal: Optional[int] = Field(default=None)
    atk: Optional[int] = Field(default=None)
    equiped: bool = False

class Use_Req(BaseModel):
    item: Item
    current_hp: int

hp = 20
power = 2
kill_count = 0

@router.get("/")
def start():
    return {"hp": hp, "kill_count": kill_count, "items": read_file(ITEM_FILE), "power": power}

@router.get("/enemy")
def get_enemy():
    global kill_count
    next_enemy = min(kill_count, len(ENEMY_DECK) - 1)
    return ENEMY_DECK[random.choice(range(next_enemy + 1))]

@router.get("/victory")
def get_prize():
    global kill_count
    kill_count += 1
    item = random.choice(ITEMS_DECK)
    item['id'] = str(uuid.uuid4())
    write_file(ITEM_FILE, item)
    return item

@router.post("/use")
def use_item(req: Use_Req):
    global hp
    global power
    current_pouch = [Item.model_validate(item) for item in read_file(ITEM_FILE)]
    if(req.item.heal):
        hp += req.item.heal
    
    if(req.item.atk):
        equiped_item = next((i for i in current_pouch if i.equiped == True), None)
        if(equiped_item):
            equiped_item.equiped = False
            power -= equiped_item.atk
            current_pouch = [i for i in current_pouch if i.id != equiped_item.id]
            current_pouch.append(equiped_item)
        if(equiped_item and equiped_item.id != req.item.id or not equiped_item):
            req.item.equiped = True
            power += req.item.atk
            print(power)
            current_pouch = [i for i in current_pouch if i.id != req.item.id]
            current_pouch.append(req.item)
    if(req.item.card_type == 'consumable'):
        hp = req.item.heal+req.current_hp
        current_pouch = [i for i in current_pouch if i.id != req.item.id]

    override_file(ITEM_FILE, [i.model_dump() for i in current_pouch])
    return {"items": current_pouch, "power": power, "hp": hp}
