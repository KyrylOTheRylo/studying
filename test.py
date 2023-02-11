import enum

import attr
from typing import List
import pymongo
from pymongo import MongoClient


class Custom_Enum(enum.Enum):
    Successful = 1
    Denied = 2
    In_process = 3


@attr.s
class Currency:
    name: str = attr.ib()


@attr.s
class TransactionDetails:
    transaction_id: str = attr.ib()
    transaction_status: Custom_Enum = attr.ib()
    currency: Currency = attr.ib()
    amount: int = attr.ib()
    recipient_id: str = attr.ib()
    mongo_client: MongoClient = attr.ib(default=None, init=False)

    def set_up_mongo_con(self, address: str = "mongodb://localhost:27017"):
        if self.mongo_client is None:
            self.mongo_client = MongoClient(address)


@attr.s
class User:
    user_id: str = attr.ib()
    transactions: List[str] = attr.ib()


a = TransactionDetails("a", [1, 2, ], Currency("USD"), 5, "ASDa")
a.set_up_mongo_con()
print(a)