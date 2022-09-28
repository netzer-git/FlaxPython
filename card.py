from typing import Callable

import triggerType


class Card:
    def __init__(self, card_id, name, power, cost, trigger_type, special_func, special_func_str):
        self._id: int = card_id
        self._name: str = name
        self._power: int = power
        self._cost: int = cost
        self._trigger_type: triggerType.CardTriggerType = trigger_type
        self._special_func: Callable = special_func
        self._special_func_str: str = special_func_str

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_power(self) -> int:
        return self._power

    def get_cost(self) -> int:
        return self._cost

    def get_trigger_type(self) -> triggerType.CardTriggerType:
        return self._trigger_type

    def get_special_func_str(self) -> str:
        return self._special_func_str

    def activate_special_func(self) -> bool:
        return self._special_func()

    def __str__(self):
        return f'{self._name} [{self._id}]: ({self._cost}), [{self._power}]\n' \
               f'{self._special_func_str if self._trigger_type is not triggerType.CardTriggerType.EMPTY else ""} '
