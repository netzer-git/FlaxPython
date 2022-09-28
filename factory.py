import area
import card
import triggerType
import random as rnd
import copy
from specialFunctions import CardFunctions
from specialFunctions import AreaFunctions

card_factory = {
    0: card.Card(0, "John Doe", 1, 1, triggerType.CardTriggerType.EMPTY, None, ""),
    1: card.Card(1, "Marry Doe", 2, 2, triggerType.CardTriggerType.EMPTY, None, "")
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
    # FIXME: returns the same object - shallow copy
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
    # FIXME: returns the same object - shallow copy
    return copy.deepcopy(area_factory[rnd.randint(1, len(area_factory) - 1)])
