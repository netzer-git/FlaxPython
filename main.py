import factory
import game
import logging
import colorama
import inputWrapper

DEBUG_MODE = True

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

FLASH_TEST_DECK = {
    "red_deck": [factory.get_card_by_id(1),
                 factory.get_card_by_id(1),
                 factory.get_card_by_id(1),
                 factory.get_card_by_id(2),
                 factory.get_card_by_id(2),
                 factory.get_card_by_id(3),
                 factory.get_card_by_id(3)],
    "blue_deck": [factory.get_card_by_id(4),
                  factory.get_card_by_id(4),
                  factory.get_card_by_id(4),
                  factory.get_card_by_id(1),
                  factory.get_card_by_id(1),
                  factory.get_card_by_id(2),
                  factory.get_card_by_id(2)]
}


def main():
    # logging mode
    if DEBUG_MODE:
        logging.basicConfig(filename='debug/debug-game.log', filemode='w', level=logging.DEBUG)
    else:
        logging.basicConfig(filename='debug/info-game.log', filemode='w', level=logging.INFO)

    logging.info('logging init')

    # auto reset all color after each print (once per print)
    colorama.init(autoreset=True)
    # input config
    inputWrapper.InputWrapper.init_input_mode("cli")
    # deck init
    decks = FLASH_TEST_DECK
    # area init
    areas = []
    # run game
    game.Game.instance().run(decks["red_deck"], decks["blue_deck"], areas)
    input()


if __name__ == '__main__':
    main()
