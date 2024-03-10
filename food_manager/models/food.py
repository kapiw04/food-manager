from dataclasses import dataclass
import time

@dataclass
class Food:
    id: int
    name: str
    expiration_date: str
    quantity: int
    opened: bool = False
    opened_date: str

    def time_to_expire(self):
        expiration_date = time.strptime(self.expiration_date, "%Y-%m-%d")
        today = time.localtime()
        return time.mktime(expiration_date) - time.mktime(today)
    
    def is_expired(self):
        return self.time_to_expire() < 0
    