from typing import List, Callable

import card
import playerColor
import logging
import triggerType


class Area:
    def __init__(self, area_id: int, name: str, trigger_type: triggerType.AreaTriggerType, special_func: Callable,
                 special_func_str: str):
        self._id: int = area_id
        self._name: str = name
        self._trigger_type: triggerType.AreaTriggerType = trigger_type
        self._special_func: Callable = special_func
        self._special_func_str: str = special_func_str

        self._red_side: List[card.Card] = []
        self._blue_side: List[card.Card] = []

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_trigger_type(self) -> triggerType.AreaTriggerType:
        return self._trigger_type

    def activate_special_func(self) -> bool:
        success = self._special_func()
        logging.debug(f'(C01) area {self._id} activated special func: {self._special_func_str}. Got {success}')
        return success

    def get_special_func_str(self) -> str:
        return self._special_func_str

    def get_side(self, color: playerColor.PlayerColor) -> List[card.Card]:
        return self._red_side if color == playerColor.PlayerColor.RED else self._blue_side

    def set_side(self, color: playerColor.PlayerColor, side: List[card.Card]) -> None:
        if color == playerColor.PlayerColor.RED:
            self._red_side = side
        else:
            self._blue_side = side

    def get_blue_side(self) -> List[card.Card]:
        return self._blue_side

    def get_side_as_str(self, player_color: playerColor.PlayerColor):
        side = self._red_side if player_color == playerColor.PlayerColor.RED else self._blue_side
        s = ""
        for c in side:
            s += " " + c.get_name() + ", "
        return s

    def get_points_from_side(self, player_color: playerColor.PlayerColor) -> int:
        return sum([c.get_power() for c in
                    (self._red_side if player_color == playerColor.PlayerColor.RED else self._blue_side)])

    def get_winner(self) -> playerColor.PlayerColor:
        isRedWinner: bool = self.get_points_from_side(playerColor.PlayerColor.RED) > self.get_points_from_side(
            playerColor.PlayerColor.BLUE)
        return playerColor.PlayerColor.RED if isRedWinner else playerColor.PlayerColor.BLUE

    def add_card_to_side(self, card: card.Card, player_color: playerColor.PlayerColor):
        self._red_side.append(card) if player_color == playerColor.PlayerColor.RED else self._blue_side.append(card)
        logging.debug(f'(C05) card: {card.get_name()} was played in area {self._id} on side {player_color}')
