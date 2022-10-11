import area
import card
import playerColor


class MetaData:

    def __init__(self):
        self.revealing_player_color: playerColor.PlayerColor = None
        self.revealing_area_index: int = None
        self.revealed_card: card.Card = None
        self.discarded_card: card.Card = None

    def get_revealing_player_color(self) -> playerColor.PlayerColor:
        return self.revealing_player_color

    def set_revealing_player_color(self, color: playerColor.PlayerColor = None):
        self.revealing_player_color = color

    def get_revealing_area_index(self) -> int:
        return self.revealing_area_index

    def set_revealing_area_index(self, new_area: area.Area = None):
        self.revealing_area_index = new_area

    def get_revealed_card(self) -> card.Card:
        return self.revealed_card

    def set_revealed_card(self, new_card: card.Card = None):
        self.revealed_card = new_card

    def get_discarded_card(self) -> card.Card:
        return self.discarded_card

    def set_discarded_card(self, new_card: card.Card = None):
        self.discarded_card = new_card
