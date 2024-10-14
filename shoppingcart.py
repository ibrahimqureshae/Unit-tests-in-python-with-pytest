from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size
        pass

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)
        pass

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for items in self.items:
            total_price += price_map.get(items)
        return total_price

  