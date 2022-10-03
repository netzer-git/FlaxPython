import area
import factory
import game
import player
import playerColor


class CardFunctions:
    @staticmethod
    def helper_get_player(get_current: bool) -> player.Player:
        if game.Game.instance().meta["revealing_player_color"] == playerColor.PlayerColor.RED:
            return game.Game.instance().red_player if get_current else game.Game.instance().blue_player
        elif game.Game.instance().meta["revealing_player_color"] == playerColor.PlayerColor.BLUE:
            return game.Game.instance().blue_player if get_current else game.Game.instance().red_player
        else:
            raise RuntimeError("Invalid current revealing player")

    @staticmethod
    def helper_get_current_played_area() -> area.Area:
        return game.Game.instance().areas[game.Game.instance().meta["revealing_area"]]

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

    @staticmethod
    def worlfsbane() -> bool:
        """On reveal: +2 power for each other card you have here"""
        current_area = CardFunctions.helper_get_current_played_area()
        side = current_area.get_side(game.Game.instance().meta["revealing_player_color"])
        current_power = game.Game.instance().meta["revealed_card"].get_power()
        game.Game.instance().meta["revealed_card"].set_power(current_power + len(side) * 2)
        return True

    @staticmethod
    def medusa() -> bool:
        """On reveal: +2 power if played in the middle area"""
        middle_area_index = 1
        if game.Game.instance().meta["revealing_area"] == middle_area_index:
            current_power = game.Game.instance().meta["revealed_card"].get_power()
            game.Game.instance().meta["revealed_card"].set_power(current_power + 2)
            return True
        else:
            return False

    @staticmethod
    def blade() -> bool:
        """On reveal: Discard a card"""
        CardFunctions.helper_get_player(True).discard_card(discard_func=None)
        return True

    @staticmethod
    def hellcow() -> bool:
        """On reveal: Discard 2 cards"""
        CardFunctions.helper_get_player(True).discard_card(discard_func=None)
        CardFunctions.helper_get_player(True).discard_card(discard_func=None)
        return True

    @staticmethod
    def apocalypse() -> bool:
        """On discard: Put it back in hand with +4 power"""
        apocalypse = game.Game.instance().meta["discarded_card"]
        apocalypse.set_power(apocalypse.get_power() + 4)
        CardFunctions.helper_get_player(True).add_card(apocalypse, True)
        return True


class AreaFunctions:

    @staticmethod
    def long_str_func() -> bool:
        """This is an area with a very lone function str"""
        return True
