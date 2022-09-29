import factory
import game
import player
import playerColor


class CardFunctions:
    @staticmethod
    def helper_get_player(get_current: bool) -> player.Player:
        if game.Game.instance().current_revealing_player == playerColor.PlayerColor.RED:
            return game.Game.instance().red_player if get_current else game.Game.instance().blue_player
        elif game.Game.instance().current_revealing_player == playerColor.PlayerColor.BLUE:
            return game.Game.instance().blue_player if get_current else game.Game.instance().red_player
        else:
            raise RuntimeError("Invalid current revealing player")

    @staticmethod
    def flash() -> bool:
        """On reveal: Draw card"""
        CardFunctions.helper_get_player(get_current=True).draw_card()
        return True

    @staticmethod
    def korg() -> bool:
        """On reveal: Shuffle a Rock to opponent deck"""
        CardFunctions.helper_get_player(get_current=False).add_card(factory.get_card_by_name("Rock"), to_hand=False)
        return True


class AreaFunctions:

    @staticmethod
    def long_str_func() -> bool:
        """This is an area with a very lone function str"""
        return True
