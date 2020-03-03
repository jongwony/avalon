from .common.role import Player
from .resistance import Merlin


class Spies(Player):
    def __init__(self, *player):
        super().__init__(*player)
        self.is_spy = True
        self.team = None

    def set_team(self):
        self.team = [x for x in self.player
                     if getattr(x, 'is_spy', None) is not None]

    def oracle(self, player):
        return player in self.team


class Assassin(Spies):
    def __init__(self, *player):
        super().__init__(*player)
        self.require = True

    @staticmethod
    def suspect(player):
        return player is Merlin


class Mordred(Spies):
    def __init__(self, *player):
        super().__init__(*player)
        self.is_spy = False


class Morgana(Spies):
    def __init__(self, *player):
        super().__init__(*player)
        self.is_merlin = True


class Oberon(Spies):
    def set_team(self):
        self.team = []


class SMinion(Spies):
    def __init__(self, *player):
        super().__init__(*player)
        self.unique = False
