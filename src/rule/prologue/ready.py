class Me:
    """
    고유 인덱스로 전역 멤버에 접근해서 역할을 정한다.
    idx is read-only
    """
    def __init__(self, idx):
        self._idx = idx
        self.role = None

    @property
    def idx(self):
        return self._idx

    def set_role(self, members):
        self.role = members[self.idx]
