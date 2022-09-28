import logging
from typing import List

import random as rnd

from colorama import Fore

import card
import game
import playerColor
import triggerType
from automaticRunner import AutomaticRunner

STARTING_HAND_SIZE = 3
STAR = "*** *** ***"
ALIGN = 25


class Player:
    def __init__(self, deck, player_color):
        self._deck: List[card.Card] = deck
        self._color: playerColor.PlayerColor = player_color
        rnd.shuffle(self._deck)
        self._hand: List[card.Card] = []
        # start with energy equal to turn num (0)
        self._energy: int = game.Game.instance().get_current_turn_energy()
        # activate cards that works on the start of the game
        for c in self._deck:
            if c.get_trigger_type() == triggerType.CardTriggerType.ON_START:
                c.activate_special_func()
                logging.debug(f'(E02) card: {c.get_id()} activated ON_START: {c.get_special_func_str()}')
        logging.debug(f'(D02) finish {self._color} creation')
        # start with STARTING_HAND_SIZE cards
        self.draw_first_hand()

    def draw_first_hand(self) -> None:
        while len(self._hand) < STARTING_HAND_SIZE and self._deck:
            self.draw_card()

    def get_player_color(self) -> playerColor.PlayerColor:
        return self._color

    def draw_card(self) -> None:
        new_card = self._deck.pop() if self._deck else None
        if new_card:
            self._hand.append(new_card)
            if new_card.get_trigger_type() == triggerType.CardTriggerType.ON_DRAW:
                new_card.activate_special_func()
                logging.debug(f'(E01) card: {new_card.get_id()} activated ON_DRAW: {new_card.get_special_func_str()}')
            logging.debug(f'(D01) {self._color} drew {new_card.get_id()}')
        else:
            logging.debug(f'(D01) {self._color} tried to draw but the deck is empty')

    def do_turn(self) -> None:
        # begin
        self.draw_card()
        self._energy = game.Game.instance().get_current_turn_energy()
        # open turn
        print(STAR)
        print(f'Energy available: {Fore.MAGENTA + str(self._energy) + Fore.RESET}')
        # show hand
        print(self.format_hand())
        # play cards
        want_to_play_card: str = AutomaticRunner.input_wrap("Do you want to play a card? (y/n): ")
        while True:
            if want_to_play_card in ["N", "n"]:
                break
            elif want_to_play_card in ["Y", "y"]:
                self.play_card()
                want_to_play_card: str = AutomaticRunner.input_wrap("Do you want to play another card? (y/n): ")
            else:
                want_to_play_card: str = AutomaticRunner.input_wrap(
                    "Invalid input. Do you want to play another card? (y/n): ")
            # TODO do we need to print hand again?

    def play_card(self) -> None:
        """
        self-sufficient function: handles all the input, and hand handling.
        """
        # get card input
        card_name_or_id = AutomaticRunner.input_wrap("Enter either Card Name or ID (Q to quit): ")
        while True:
            card_index = -1
            for i in range(len(self._hand)):
                if card_name_or_id == self._hand[i].get_name() or card_name_or_id == str(self._hand[i].get_id()):
                    card_index = i
                    break
                    # want to quit
            if card_name_or_id in ['q', 'Q']:
                return
            # energy check for the found card
            elif card_index != -1 and self._hand[card_index].get_cost() <= self._energy:
                break
            # failed energy check
            elif card_index != -1 and self._hand[card_index].get_cost() > self._energy:
                card_name_or_id = AutomaticRunner.input_wrap("You don't have enough energy to play this card: ")
            # wrong input
            else:
                card_name_or_id = AutomaticRunner.input_wrap(
                    "Card Name or ID are not matching any cards in hand: ")
        # get area input:
        area_index: int = int(AutomaticRunner.input_wrap("Enter Area index: "))
        while True:
            if area_index in [1, 2, 3] and game.Game.instance().is_card_playable_in_area(self._hand[card_index],
                                                                                         area_index):
                break
            else:
                area_index = int(AutomaticRunner.input_wrap("Invalid Area number, please enter 1, 2, 3: "))

        card_to_play: card.Card = self._hand.pop(card_index)
        self._energy = self._energy - card_to_play.get_cost()
        game.Game.instance().play_card_in_area(card_to_play, area_index, self._color)

    def add_card(self, card: card.Card, to_hand: bool) -> None:
        if to_hand:
            self._hand.append(card)
        else:
            self._deck.append(card)
            rnd.shuffle(self._deck)

    def format_hand(self) -> str:
        if not self._hand:
            return ""
        hand_str_lst = []
        colorama = Fore.RED if self._color == playerColor.PlayerColor.RED else Fore.BLUE
        for a in self._hand:
            hand_str_lst.append([f'{colorama + "-" * ALIGN + Fore.RESET}',
                                 f'{a.get_name()} ({a.get_id()})',
                                 '*',
                                 f'{a.get_special_func_str()}',
                                 '*',
                                 f'{a.get_cost()}c|{a.get_power()}p',
                                 f'{colorama + "-" * ALIGN + Fore.RESET}'])
        full_str = ""
        for i in range(len(hand_str_lst[0])):
            # ALIGN = 20
            for j in range(len(hand_str_lst)):
                full_str += f'{colorama + "| " + Fore.RESET}{hand_str_lst[j][i] : ^{ALIGN}}{colorama + "| " + Fore.RESET}'
            full_str += "\n"
        return full_str
