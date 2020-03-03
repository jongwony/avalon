class Player:
    def __init__(self, *player):
        self.player = player
        self.leader = False
        self.opinion = None
        self.quest = None

    def choose(self, *player):
        """
        본인이 대장(turn)이라면 원정대(party)를 꾸린다
        """
        if not self.leader:
            return
        return player

    def vote(self, opinion):
        """
        찬성 또는 반대를 제출한다.
        """
        self.opinion = opinion
        return self.opinion

    def mission(self, quest):
        """
        성공 또는 실패를 제출한다.
        """
        self.quest = quest
        return self.quest
