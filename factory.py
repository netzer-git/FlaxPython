import area
import card
import triggerType
import random as rnd
import copy
from specialFunctions import CardFunctions
from specialFunctions import AreaFunctions

card_factory = {
    0: card.Card(0, "Rock", 0, 1, triggerType.CardTriggerType.EMPTY, None, "Let's Rock"),
    1: card.Card(1, "Misty Knight", 2, 1, triggerType.CardTriggerType.EMPTY, None, ""),
    2: card.Card(2, "The Flash", 1, 1, triggerType.CardTriggerType.ON_REVEAL,
                 CardFunctions.flash,
                 CardFunctions.flash.__doc__),
    3: card.Card(3, "Korg", 2, 1, triggerType.CardTriggerType.ON_REVEAL,
                 CardFunctions.korg,
                 CardFunctions.korg.__doc__),
    4: card.Card(4, "Wolfsbane", 1, 3, triggerType.CardTriggerType.ON_REVEAL,
                 CardFunctions.worlfsbane,
                 CardFunctions.worlfsbane.__doc__),
    5: card.Card(5, "Medusa", 2, 2, triggerType.CardTriggerType.ON_REVEAL,
                 CardFunctions.medusa,
                 CardFunctions.medusa.__doc__)
}

area_factory = {
    0: area.Area(0, "Empty", triggerType.AreaTriggerType.EMPTY, None, ""),
    1: area.Area(1, "After-Empty", triggerType.AreaTriggerType.EMPTY, None, ""),
    2: area.Area(2, "Long-Empty", triggerType.AreaTriggerType.EMPTY,
                 AreaFunctions.long_str_func,
                 AreaFunctions.long_str_func.__doc__),
}


def get_card_by_name(name: str) -> card.Card:
    for k in card_factory:
        if name == card_factory[k].get_name():
            return copy.deepcopy(card_factory[k])
    raise ValueError(f'Card name {name} not found in the factory')


def get_card_by_id(card_id: int) -> card.Card:
    if card_id in card_factory:
        return copy.deepcopy(card_factory[card_id])
    raise ValueError(f'Card id {card_id} not found in the factory')


def get_random_card() -> card.Card:
    return copy.deepcopy(card_factory[rnd.randint(1, len(card_factory) - 1)])


def get_area_by_name(name: str) -> area.Area:
    for k in area_factory:
        if name == area_factory[k].get_name():
            return copy.deepcopy(area_factory[k])
    raise ValueError(f'Area name {name} not found in the factory')


def get_area_by_id(area_id: int) -> area.Area:
    if area_id in area_factory:
        return copy.deepcopy(area_factory[area_id])
    raise ValueError(f'Card id {area_id} not found in the factory')


def get_random_area() -> area.Area:
    return copy.deepcopy(area_factory[rnd.randint(1, len(area_factory) - 1)])
