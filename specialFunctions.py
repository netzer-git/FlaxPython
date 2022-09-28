import game
import player
import playerColor


class CardFunctions:
    @staticmethod
    def helper_get_current_player() -> player.Player:
        if game.Game.instance().current_revealing_player == playerColor.PlayerColor.RED:
            return game.Game.instance().red_player
        elif game.Game.instance().current_revealing_player == playerColor.PlayerColor.BLUE:
            return game.Game.instance().blue_player
        else:
            raise RuntimeError("Invalid current revealing player")

    @staticmethod
    def flash() -> bool:
        """On reveal: Draw card"""
        CardFunctions.helper_get_current_player().draw_card()
        return True


class AreaFunctions:

    @staticmethod
    def long_str_func() -> bool:
        """This is an area with a very lone function str"""
        return True
