import factory
import game
import logging
import colorama

DEBUG_MODE = True


def main():
    # logging mode
    if DEBUG_MODE:
        logging.basicConfig(filename='debug/debug-game.log', filemode='w', level=logging.DEBUG)
    else:
        logging.basicConfig(filename='debug/info-game.log', filemode='w', level=logging.INFO)

    logging.info('logging init')

    # auto reset all color after each print (once per print)
    colorama.init(autoreset=True)

    # deck init
    red_deck = [factory.get_card_by_id(0),
                factory.get_card_by_id(0),
                factory.get_card_by_id(0),
                factory.get_card_by_id(1),
                factory.get_card_by_id(1)]
    blue_deck = [factory.get_card_by_id(0),
                 factory.get_card_by_id(0),
                 factory.get_card_by_id(0),
                 factory.get_card_by_id(1),
                 factory.get_card_by_id(1)]
    # area init
    areas = []
    # init game
    game.Game.instance().init_game(red_deck, blue_deck, areas)
    # run game
    game.Game.instance().run_game()
    # finish game
    game.Game.instance().end_game()
    input()


if __name__ == '__main__':
    main()
