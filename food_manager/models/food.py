from dataclasses import dataclass
import time

@dataclass
class Food:
    id: int
    name: str
    expiration_date: str
    quantity: int
    opened: bool = False
    opened_date: str = None

    def time_to_expire(self):
        expiration_date = time.strptime(self.expiration_date, "%d-%m-%Y")
        print(expiration_date)
        today = time.localtime()
        print(today)
        return (time.mktime(expiration_date) - time.mktime(today)) // 86400
    
    def is_expired(self):
        return self.time_to_expire() < 0
    