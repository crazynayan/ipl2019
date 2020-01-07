from typing import Optional

from firestore_ci import FirestoreDocument


class Player(FirestoreDocument):

    def __init__(self):
        super().__init__()
        self.name: str = str()
        self.owners: list = list()
        self.price1: int = 0
        self.price2: int = 0
        self.owner1: Optional[str] = None
        self.owner2: Optional[str] = None
        self.cost: int = 0
        self.base: int = 0
        self.country: str = str()
        self.type: str = str()
        self.score: float = 0.0
        self.team: str = str()
        self.bid_order1: int = 0
        self.bid_order2: int = 0
        self.bids1: dict = dict()
        self.bids2: dict = dict()


Player.init()
