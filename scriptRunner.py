import logging
from typing import List
import colorama
import playerColor
import factory
import game

DEBUG_MODE = True
SCRIPT_RUNNER_MODE = False

EASY_TEST_INPUT = [
    ["red1", "y", "0", "1", "n"],
    ["blue1", "y", "0", "2", "n"],
    ["red2", "y", "1", "1", "n"],
    ["blue2", "y", "1", "3", "n"],
    ["red3", "y", "0", "3", "n"],
    ["blue3", "n"],
    ["red4", "y", "0", "2", "n"],
    ["blue4", "n"],
    ["red5", "n"],
    ["blue5", "y", "1", "3", "n"],
    ["red6", "y", "1", "2", "n"],
    ["blue6", "n"]
]

EASY_TEST_DECK = {
    "red_deck": [factory.get_card_by_id(0),
                 factory.get_card_by_id(0),
                 factory.get_card_by_id(0),
                 factory.get_card_by_id(1),
                 factory.get_card_by_id(1)],
    "blue_deck": [factory.get_card_by_id(0),
                  factory.get_card_by_id(0),
                  factory.get_card_by_id(0),
                  factory.get_card_by_id(1),
                  factory.get_card_by_id(1)]
}


class ScriptedRunner:
    turn: int = 0
    inside_turn: int = 0
    turn_logger: playerColor.PlayerColor = playerColor.PlayerColor.RED
    # TODO: add script here
    script: List[List[str]] = None

    @staticmethod
    def init_script(script):
        ScriptedRunner.script = script

    @staticmethod
    def input_wrap(prompt: str) -> str:
        # scripted input - test purposes
        if SCRIPT_RUNNER_MODE:
            scripted_input = ScriptedRunner.script[ScriptedRunner.turn][ScriptedRunner.inside_turn]
            ScriptedRunner.inside_turn += 1
            # end of turn
            if ScriptedRunner.inside_turn == len(ScriptedRunner.script[ScriptedRunner.turn]):
                ScriptedRunner.turn += 1
                ScriptedRunner.inside_turn = 0
            if scripted_input == 'n':
                ScriptedRunner.turn_logger = playerColor.PlayerColor.RED if ScriptedRunner.turn_logger == playerColor.PlayerColor.BLUE else playerColor.PlayerColor.BLUE
            return scripted_input
        # regular input
        else:
            return input(prompt)


def main_wrapper(script_name):
    # logging mode
    if DEBUG_MODE:
        logging.basicConfig(filename='debug/scripted-debug-game.log', filemode='w', level=logging.DEBUG)
    else:
        logging.basicConfig(filename='debug/scripted-info-game.log', filemode='w', level=logging.INFO)

    logging.info('logging init')
    logging.info('Running scripted game')
    logging.info(f'script_name: {script_name}')

    ScriptedRunner.init_script(EASY_TEST_INPUT)

    areas = []
    decks = EASY_TEST_DECK

    # auto reset all color after each print (once per print)
    colorama.init(autoreset=True)
    # run game
    game.Game.instance().run(decks["red_deck"], decks["blue_deck"], areas)


if __name__ == '__main__':
    main_wrapper("easy_script")
