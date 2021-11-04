from dataclasses import dataclass
from typing import Optional, Set
from datetime import date

'''
Dataclass are great for value object.

An order line is uniquely identified by its order ID, SKU, and quantity; if we 
change one of those values, we now have a new line. That’s the definition of a
value object: any object that is identified only by its data and doesn’t have
a long-lived identity
'''

'''
Optional 

Note that this is not the same concept as an optional argument, which is one
that has a default. An optional argument with a default does not require the
Optional qualifier on its type annotation just because it is optional.
On the other hand, if an explicit value of None is allowed, the use of Optional
is appropriate, whether the argument is optional or not.
'''


@dataclass(frozen=True)
class Orderline:
    orderid : str
    sku : str
    qty : int

class Batch:
    def __init__(self, reference: str, sku: str, quantity: int, eta: Optional[date]) -> None:
        self.reference = reference
        self.sku = sku
        self._purchased_quantity = quantity
        self.eta = eta
        self._allocations = Set()

    def __repr__(self) -> str:
        return "<Batch {ref}>".format(ref=self.reference)

    def __hash__(self) -> int:
        return(hash(self.reference))

    def __gt__(self,other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta
    
    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)
    
    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: Orderline) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
    
    def allocate(self, line: Orderline) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line) -> None:
        if line in self._allocations:
            self._allocations.remove(line)