from .common.role import Player


class Resistance(Player):
    def __init__(self, *player):
        super().__init__(*player)
        self.is_resistance = True


class Merlin(Resistance):
    def __init__(self, *player):
        super().__init__(*player)
        self.spies = None
        self.is_merlin = True
        self.require = True

    def set_spies(self):
        self.spies = [x for x in self.player if getattr(x, 'is_spy', False)]

    def oracle(self, player):
        return player in self.spies


class Percival(Resistance):
    def __init__(self, *player):
        super().__init__(*player)
        self.merlin = None

    def set_merlin(self):
        self.merlin = [x for x in self.player if getattr(x, 'is_merlin', False)]

    def oracle(self, player):
        return player in self.merlin


class RMinion(Resistance):
    def __init__(self, *player):
        super().__init__(*player)
        self.unique = False
