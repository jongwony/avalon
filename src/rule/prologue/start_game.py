import random

from src.player.resistance import Merlin, Percival, RMinion
from src.player.spies import Mordred, Morgana, Assassin, Oberon, SMinion


class Members:
    def __init__(self, count):
        assert 5 <= count <= 10
        self._members = None
        self.count = count

    @property
    def members(self):
        return self._members

    def recommend(self):
        return {
            5: [Merlin, RMinion, RMinion, Assassin, SMinion],
            6: [[Merlin, RMinion, RMinion, RMinion, Assassin, SMinion],
                [Merlin, Percival, RMinion, RMinion, Assassin, Morgana]],
            7: [[Merlin, Percival, RMinion, RMinion, Assassin, Morgana, Oberon],
                [Merlin, Percival, RMinion, RMinion, Assassin, SMinion, SMinion]],
            8: [[Merlin, Percival, RMinion, RMinion, RMinion, Assassin, Morgana, Oberon],
                [Merlin, Percival, RMinion, RMinion, RMinion, Assassin, SMinion, SMinion]],
            9: [[Merlin, Percival, RMinion, RMinion, RMinion, RMinion, Assassin, Morgana, Mordred],
                [Merlin, Percival, RMinion, RMinion, RMinion, RMinion, Assassin, Morgana, SMinion]],
            10: [Merlin, Percival, RMinion, RMinion, RMinion, RMinion, Assassin, Morgana, Mordred, SMinion],
        }[self.count]

    def choose(self, n):
        temp = self.recommend()
        if len(temp) >= 1:
            self._members = temp[n]
        else:
            self._members = temp
        return self.members

    def custom(self, *role):
        self._members = [Merlin, Assassin, *role]
        return self.members

    def shuffle(self):
        random.shuffle(self.members)
