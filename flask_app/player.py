from typing import Optional

from firestore_ci import FirestoreDocument


class Player(FirestoreDocument):

    def __init__(self):
        super().__init__()
        self.name: str = str()
        self.price: int = 0
        self.owner: Optional[str] = None
        self.cost: int = 0
        self.base: int = 0
        self.country: str = str()
        self.type: str = str()
        self.score: float = 0.0
        self.team: str = str()
        self.bid_order: int = 0
        self.bids: dict = dict()


Player.init()
