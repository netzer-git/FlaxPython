from enum import Enum


class CardTriggerType(Enum):
    EMPTY = 0
    ON_REVEAL = 1
    ON_GOING = 2
    ON_DRAW = 3
    ON_DESTROY = 4
    ON_START = 5
    ON_END = 6
    ON_DISCARD = 7
    ON_MOVE = 8


class AreaTriggerType(Enum):
    EMPTY = 0
    ON_REVEAL = 1
    ON_GOING = 2
