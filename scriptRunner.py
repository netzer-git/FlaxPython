import factory
import game
import logging
import colorama
import inputWrapper

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

MEDUSA_TEST_INPUT = [
    ["red1", "n"],
    ["blue1", "n"],
    ["red2", "y", "5", "2", "n"],
    ["blue2", "y", "5", "3", "n"],
]

MEDUSA_DECK = {
    "red_deck": [factory.get_card_by_id(0),
                 factory.get_card_by_id(1),
                 factory.get_card_by_id(5)],
    "blue_deck": [factory.get_card_by_id(0),
                  factory.get_card_by_id(0),
                  factory.get_card_by_id(5)]
}

DISCARD_TEST_INPUT = [
    ["red1", "y", "6", "1", "n"],
    ["blue1", "n"],
    ["red2", "n"],
    ["blue2", "y", "1", "3", "n"],
    ["red3", "n"],
    ["blue3", "n"],
    ["red4", "y", "7", "2", "n"],
    ["blue4", "n"],
    ["red5", "n"],
    ["blue5", "n"],
    ["red6", "y", "8", "3", "n"],
    ["blue6", "n"]
]

DISCARD_DECK = {
    "red_deck": [factory.get_card_by_id(6),
                 factory.get_card_by_id(7),
                 factory.get_card_by_id(8),
                 factory.get_card_by_id(1)],
    "blue_deck": [factory.get_card_by_id(0),
                  factory.get_card_by_id(1),
                  factory.get_card_by_id(1),
                  factory.get_card_by_id(1)]
}


def main_wrapper(script_name):
    # logging mode
    if DEBUG_MODE:
        logging.basicConfig(filename='debug/scripted-debug-game.log', filemode='w', level=logging.DEBUG)
    else:
        logging.basicConfig(filename='debug/scripted-info-game.log', filemode='w', level=logging.INFO)

    logging.info('logging init')
    logging.info('Running scripted game')
    logging.info(f'script_name: {script_name}')

    inputWrapper.InputWrapper.init_input_mode("scripted")
    # TODO: update on use
    inputWrapper.InputWrapper.init_script(DISCARD_TEST_INPUT)

    areas = []
    # TODO: update on use
    decks = DISCARD_DECK

    # auto reset all color after each print (once per print)
    colorama.init(autoreset=True)
    # run game
    game.Game.instance().run(decks["red_deck"], decks["blue_deck"], areas)


if __name__ == '__main__':
    main_wrapper("easy_script")
