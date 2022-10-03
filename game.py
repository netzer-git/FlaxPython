from typing import List, Dict
import logging

import card
import area
import player
import playerColor as pc
import factory
import triggerType
from singleton import Singleton
from colorama import Fore

STAR = "*** *** ***"
DASH = "--- --- ---"
ALIGN = 50


@Singleton
class Game:
    def __init__(self):
        self._turn_num: int = 0
        self.areas: List[area.Area] = []
        self._game_finish: int = 6

        self.red_player: player.Player = None
        self.blue_player: player.Player = None
        self._red_card_queue = []
        self._blue_card_queue = []

        # used only in revealing stage - creating metadata for cards special function
        self.meta: Dict[str, any] = {
            "revealing_player_color": None,
            "revealing_area": None,
            "revealed_card": None,
            "discarded_card": None
        }

    def get_current_turn_energy(self) -> int:
        # TODO: change with area changes
        return self._turn_num

    def get_current_turn_num(self) -> int:
        return self._turn_num

    def is_card_playable_in_area(self, card: card.Card, area_index: int) -> bool:
        # TODO: change with area changes
        return True

    def get_current_winner(self) -> pc.PlayerColor:
        red_sum: int = 0
        red_wins: int = 0
        blue_sum: int = 0
        blue_wins: int = 0
        for a in self.areas:
            if a.get_scoreboard() > 0:
                red_wins += 1
                red_sum += a.get_scoreboard()
            elif a.get_scoreboard() < 0:
                blue_wins += 1
                blue_sum += -a.get_scoreboard()
        if red_wins > blue_wins or (red_wins == blue_wins and red_sum > blue_sum):
            return pc.PlayerColor.RED
        else:
            return pc.PlayerColor.BLUE

    def roll_new_area(self, area_index: int) -> None:
        # save areas
        red_side = self.areas[area_index].get_side(pc.PlayerColor.RED)
        blue_side = self.areas[area_index].get_side(pc.PlayerColor.BLUE)
        # roll new area
        self.areas[area_index] = factory.get_random_area()
        # refill areas
        self.areas[area_index].set_side(pc.PlayerColor.RED, red_side)
        self.areas[area_index].set_side(pc.PlayerColor.BLUE, blue_side)
        # reveal area
        if self.areas[area_index].get_trigger_type() == triggerType.AreaTriggerType.ON_REVEAL:
            self.areas[area_index].activate_special_func()
            logging.debug(
                f'(F01) area: {self.areas[area_index].get_id()} activated ON_REVEAL: {self.areas[area_index].get_special_func_str()}')
        logging.debug(
            f'(B05) area (index {area_index} id {self.areas[area_index].get_id()}) was rolled, filled and revealed')

    def play_card_in_area(self, card: card.Card, area_index: int, player_color: pc.PlayerColor) -> None:
        if player_color == pc.PlayerColor.RED:
            self._red_card_queue.append((card, area_index))
            logging.debug(f'(B03) card: {card.get_id()} was played to area {area_index} for player {player_color}')
        else:
            self._blue_card_queue.append((card, area_index))
            logging.debug(f'(B03) card: {card.get_id()} was played to area {area_index} for player {player_color}')

    def play_all_cards_in_queue(self, player_color: pc.PlayerColor):
        player_queue = self._red_card_queue if player_color == pc.PlayerColor.RED else self._blue_card_queue
        self.meta["revealing_player_color"] = player_color  # card metadata
        for c in player_queue:
            self.meta["revealed_card"] = c[0]
            if c[0].get_trigger_type() == triggerType.CardTriggerType.ON_REVEAL:
                self.meta["revealing_area"] = c[1] - 1  # card metadata
                c[0].activate_special_func()
                logging.debug(f'(E02) card: {c[0].get_id()} activated ON_REVEAL: {c[0].get_special_func_str()}')
                self.meta["revealing_area"] = None  # clear card metadata
            self.areas[c[1] - 1].add_card_to_side(c[0], player_color)
            logging.debug(f'(B01) card: {c[0].get_id()} was added to area {c[1]} for player {player_color}')
            self.meta["revealed_card"] = None
        self.meta["revealing_player_color"] = None  # clear card metadata

    def init_game(self, red_deck: List[card.Card], blue_deck: List[card.Card], areas: List[area.Area] = None):
        logging.info('init game')
        logging.debug('init areas to empty areas')
        self.areas = areas if areas else [factory.get_area_by_id(0),
                                          factory.get_area_by_id(0),
                                          factory.get_area_by_id(0)]
        logging.debug('init players')
        self.red_player = player.Player(red_deck, pc.PlayerColor.RED)
        logging.debug(f'red player: {self.red_player}')
        self.blue_player = player.Player(blue_deck, pc.PlayerColor.BLUE)
        logging.debug(f'blue player: {self.blue_player}')

    def end_game(self) -> pc.PlayerColor:
        """
        run the end of the game, have to be after run_game
        """
        logging.info('end game')
        winner: pc.PlayerColor = self.get_current_winner()
        colorama = Fore.RED if winner == pc.PlayerColor.RED else Fore.BLUE
        winner_str = "RED" if winner == pc.PlayerColor.RED else "BLUE"
        print(self.format_areas())
        print()
        print()
        print("The winner is " + colorama + "**** " + winner_str + " ****" + Fore.RESET)
        print()
        print()
        return winner

    def run_turn(self) -> None:
        logging.debug(f'print areas')
        print(self.format_areas())

        logging.info(f'start turn {self._turn_num}')
        print(DASH)
        print(Fore.RED + "Red Player Turn: " + Fore.RESET)
        self.red_player.do_turn()
        print(DASH)
        print(Fore.BLUE + "Blue Player Turn: " + Fore.RESET)
        self.blue_player.do_turn()
        print(DASH)

        logging.debug(f'(B02) conclude turn {self._turn_num}')
        starting_color: pc.PlayerColor = self.get_current_winner()
        other_color: pc.PlayerColor = pc.PlayerColor.RED if starting_color == pc.PlayerColor.BLUE else pc.PlayerColor.BLUE
        logging.debug(f'(B02) {starting_color} is the current winner, plays his queue first')
        self.play_all_cards_in_queue(starting_color)
        logging.debug(f'(B02) {other_color} is the current loser, plays his queue second')
        self.play_all_cards_in_queue(other_color)
        logging.debug(f'(B02) clear queues')
        self._red_card_queue = []
        self._blue_card_queue = []

    def main_game(self) -> None:
        """
        run the whole turns of the game, have to be after init_game
        """
        logging.info('run game')
        while True:
            self._turn_num += 1
            if self._turn_num > self._game_finish:
                logging.debug(f'Got to the furn after the last turn: {self._turn_num}')
                return
            elif self._turn_num <= 3 and self.areas[self._turn_num - 1].get_id() == 0:
                self.roll_new_area(self._turn_num - 1)
                logging.debug(f'(B04) reveal area: {self.areas[self._turn_num - 1].get_name()}')
            self.run_turn()

    def run(self, red_deck: List[card.Card], blue_deck: List[card.Card], areas: List[area.Area]) -> None:
        """Main game running function"""
        # init game
        self.init_game(red_deck, blue_deck, areas)
        # run game
        self.main_game()
        # finish game
        self.end_game()

    def format_areas(self) -> str:
        area_str_lst = []
        for a in self.areas:
            red_side_str = a.get_side_as_str(pc.PlayerColor.RED)
            blue_side_str = a.get_side_as_str(pc.PlayerColor.BLUE)
            max_a_row: int = max(len(a.get_name()),
                                 len(a.get_special_func_str()),
                                 len(red_side_str),
                                 len(blue_side_str)) + 2
            area_str_lst.append([Fore.RED + '-' * ALIGN + Fore.RESET,
                                 f'{red_side_str}',
                                 f'{a.get_points_from_side(pc.PlayerColor.RED)}',
                                 '***',
                                 f'{a.get_name()}',
                                 f'{a.get_special_func_str()}',
                                 '***',
                                 f'{a.get_points_from_side(pc.PlayerColor.BLUE)}',
                                 f'{blue_side_str}',
                                 Fore.BLUE + '-' * ALIGN + Fore.RESET])
        full_str = ""
        for i in range(len(area_str_lst[0])):
            # ALIGN = 20
            for j in range(len(area_str_lst)):
                full_str += f'|{area_str_lst[j][i] : ^{ALIGN}}'
            full_str += "|\n"
        return full_str
